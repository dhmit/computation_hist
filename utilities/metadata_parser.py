# python
import csv
import sqlite3

# ext
from pdf2image import convert_from_path

# django
from django.db import IntegrityError
from django.core.exceptions import ValidationError
from django.utils.text import slugify

# project
from config.settings import METADATA_CSV, DATABASES
from apps.archives.models import (
    Organization,
    Person,
    Box,
    Folder,
    Document,
    Page,
)
from .common import get_file_path

from .name_parser import PeopleDatabase



def populate_from_metadata(metadata_filename=None):
    '''
    :param metadata_filename: is a path to a csv file (relative or actual)
    :return: populates the django database, but returns nothing
    how to run:
    open up terminal (with virtual environment):
    > cd djweb
    > python manage.py shell
    in shell:
    > from utilities.metadata_parser import populate_from_metadata
    > populate_from_metadata()
    The 'r' in front of the file location isn't necessary but can help to prevent strange errors.
    Utilizes interpret_organization_person to add authors, recipients, and cced.
    '''

    if metadata_filename is None:
        metadata_filename = METADATA_CSV

    # the aliases_to_full_name_dict maps from raw (csv) names to authoritative full names, e.g.
    # e.g. 'Corbatò, F. J.' -> 'Corbató, Fernando J.'
    people_db = PeopleDatabase()
    people_db.extract_names_from_metadata_sheet()
    aliases_to_full_name_dict = people_db.get_aliases_to_full_name_dict()

    with open(metadata_filename) as file:
        csv_file = csv.DictReader(file)
        count_added = 0
        count_skipped = 0
        count_invalid = 0
        names = {}
        for line_id, line in enumerate(csv_file):
            # Skip empty lines
            if "".join(line.values()) == '':
                continue

            missing_metadata = []
            for attr in ['box', 'folder_number', 'doc_id', 'filename', 'author',
                         'title', 'first_page', 'last_page']:
                if not line[attr]:
                    missing_metadata.append(attr)

            if missing_metadata:
                print(f'WARNING: Line {line_id+1} is incomplete (skipping).\
                        \n\tMissing fields: {missing_metadata} - FIXME in the metadata!')
                count_skipped += 1
                continue

            try:
                add_one_document(line, aliases_to_full_name_dict, line_id+1, names)
                count_added += 1
            except ValidationError as e:
                count_invalid += 1
                print(f'{e}. Line: {line}.')


    print(f'''\n################################################################################
    IMPORT COMPLETE
################################################################################
    Added {count_added} documents from {metadata_filename}.
    Skipped {count_skipped} documents because of incomplete metadata.
    {count_invalid} had invalid data.\r\n''')
    # display name variants for manual fixing with the help of Ctrl-F
    # may be too long to fit in PyCharm terminal, so you may have to write to file
    print(f'''NAME VARIANTS\r\n''')
    for last_name in sorted(list(names.keys())):
        if len(names[last_name]) > 1:
            print("Last name:")
            print("\t" + last_name)
            first_names = sorted(list(names[last_name]), key=lambda name: (name[0] if len(name) > 0 else '', -len(name)))
            print("First name variants:")
            for first_name in first_names:
                print("\t" + first_name)
            print("")

def add_one_document(csv_line, aliases_to_full_name_dict, line_no=None, names={}):
    """
    Processes one line from a metadata csv file and add it to the database.
    Note: This function does not check if the metadata is complete. It is only supposed to be
    accessed by populate_from_metadata.

    >>> from collections import OrderedDict
    >>> csv_line = OrderedDict([('box', '1'), ('folder_number', '1'), ('foldername_short',
    ... 'committee_on_machine_methods'), ('foldername_full', 'Committee on Machine Methods'),
    ... ('doc_id', '17'), ('filename', '1_1_committee_on_machine_methods_17'),
    ... ('author', 'Morse, Philip M.'), ('title', 'Minutes of the Seventeenth...'),
    ... ('date', '1951-05-16'), ('first_page', '29'), ('last_page', '29'),
    ... ('metadata_added_by', 'mingfei'), ('doc_type', 'minutes'), ('recipients', 'unknown'),
    ... ('cced', 'unknown'), ('notes', ''), ('metadata_specialist_notes', '')])
    >>> add_one_document(csv_line)
    :param csv_line: OrderedDict
    :param line_no: int
    :param names: dict
    :return:
    """

    # NOTE(ra): number of pages
    number_of_pages = int(csv_line['last_page']) - int(csv_line['first_page']) + 1
    file_name = csv_line['filename']
    slug = slugify(file_name)
    new_doc = Document(number_of_pages=number_of_pages,
                       title=csv_line['title'],
                       type=csv_line['doc_type'],
                       notes=csv_line['notes'],
                       first_page=csv_line['first_page'],  # should this be an int?
                       last_page=csv_line['last_page'],
                       file_name=file_name,
                       slug=slug)

    txt_path = get_file_path(box=int(csv_line['box']), folder=int(csv_line['folder_number']),
                             foldername_short=csv_line['foldername_short'],
                             doc_id=csv_line['doc_id'], path_type='absolute', file_type='txt')
    try:
        with open(txt_path, 'r', encoding='utf8') as f:
            new_doc.text = f.read()
    except FileNotFoundError:
        print(f'skipped {txt_path}')
        new_doc.text = ''


    # Date
    if csv_line['date'] != '' and csv_line['date'][0] == '1':
        new_doc.date = csv_line['date']


    # Folder 
    box_num = csv_line['box']
    new_box, _unused_box_exist = Box.objects.get_or_create(number=box_num)

    folder_name = csv_line['foldername_short']

    new_folder, folder_exist = Folder.objects.get_or_create(
        name=folder_name,
        defaults={
            'box': new_box,
            'number': csv_line['folder_number'],
            'full': csv_line['foldername_full'],
        }
    )

    new_doc.folder = new_folder


    # Author, Recipient, cced

    # This would be better with create_or_update so that changed values get updated.
    # Not super important, though, as flushing the db will also update the values
    try:
        new_doc.save()

        interpret_person_organization(csv_line['author'],
                                      "author_organization",
                                      "author_person",
                                      new_doc,
                                      aliases_to_full_name_dict,
                                      line_no,
                                      names,
                                      )
        interpret_person_organization(csv_line['recipients'],
                                      "recipient_organization",
                                      "recipient_person",
                                      new_doc,
                                      aliases_to_full_name_dict,
                                      line_no,
                                      names,
                                      )
        interpret_person_organization(csv_line['cced'],
                                      "cced_organization",
                                      "cced_person",
                                      new_doc,
                                      aliases_to_full_name_dict,
                                      line_no,
                                      names,
                                      )
        new_doc.save()
    except IntegrityError:
        pass


def pdf_to_image_split(pdf_path, image_directory, folder_name):
    """
    Splits a each page of a pdf into an image.
    pdf_path is the location of pdf (C:\Documents\rockefeller.pdf)
    image_directory is the location of image folder (C:\Documents\png_pages\)
    folder_name is the names of the object of the folder(rockefeller)
    """
    pages = convert_from_path(pdf_path)
    images_in_pdf = []

    for page in range(len(pages)):
        page_path = image_directory + folder_name + '_' + str(page + 1) + '.png'
        pages[page].save(page_path, 'PNG')
        images_in_pdf.append((page_path, page +1))

    return images_in_pdf


def page_image_to_doc(folder_name, pdf_path, image_directory):
    """
    Utilizes pdf_to_image_split in order to create images of Pages from a pdf, create Page
    objects, and assign those page objects to Document.
    Splits a each page of a pdf into an image.
    pdf_path is the location of pdf (C:\Documents\rockefeller.pdf)
    image_directory is the location of image folder (C:\Documents\png_pages\)
    folder_name is the names of the object of the folder(rockefeller)
    Example: page_image_to_doc('rockefeller', 'C:\Documents\1_08_raw_rockefeller.pdf',
    'C:\Documents\png_pages\') returns images of Pages in png_pages directory and Page objects
    of each page.
    """
    images_in_pdf = pdf_to_image_split(pdf_path, image_directory, folder_name)
    folder = Folder.objects.get(name=folder_name)
    documents_unsort = folder.document_set.all()
    documents_sort = sorted(documents_unsort, key=lambda x: x.first_page)
    document_place = 0
    page_num = 1

    for page in images_in_pdf:
        if documents_sort[document_place].first_page <= page[1] <= documents_sort[ \
                document_place].last_page:
            # this means that this is the same document as last page
            page_obj = Page(document=documents_sort[document_place], page_number=page_num)
            page_obj.image_path.name = folder_name + '_' + str(page[1]) + '.png'
            page_obj.save()
            page_num += 1
        elif documents_sort[document_place +1].first_page <= page[1] <= documents_sort[ \
                document_place +1].last_page:
            # this means this is a new document
            document_place += 1
            page_num = 1
            page_obj = Page(document=documents_sort[document_place], page_number=page_num)
            page_obj.image_path.name = folder_name + '_' + str(page[1]) + '.png'
            page_obj.save()
            page_num += 1
        else:
            # This means that the page isn't associated with a document
            pass


def interpret_person_organization(field, item_organization, item_person, new_doc,
                                  aliases_to_full_name_dict, line_no=None, names_so_far={}):

    # Adds people and organizations as an author, recipient, or CC'ed.
    field_split = [person_or_organization.strip() for person_or_organization in field.split(';')]

    for person_or_organization in field_split:
        if len(person_or_organization.split(',')) == 1:
            new_org, _unused_org_created = Organization.objects.get_or_create(name=field_split[0])
            bound_attr = getattr(new_doc, item_organization)
            bound_attr.add(new_org)
        else:
            split_name = person_or_organization.split(',')
            # check for commas
            if len(split_name) > 2:
                print("There seem to be too many commas in this name", split_name, "in line",
                      line_no)
            else:
                last_name, first_name = aliases_to_full_name_dict[person_or_organization].split(',')
                if last_name == 'unknown':
                    last_name = ''
                if first_name == 'unknown':
                    first_name = ''

                #            # add first name, last name pair to names
                if last_name != '':
#                    unfixed_first_name = split_name[1].strip()
                    if last_name not in names_so_far:
                        names_so_far[last_name] = {first_name}
                    else:
                        names_so_far[last_name].add(first_name)

                new_person, _unused_person_created = Person.objects.get_or_create(
                    last=last_name,
                    first=first_name,
                )

                bound_attr = getattr(new_doc, item_person)
                bound_attr.add(new_person)


