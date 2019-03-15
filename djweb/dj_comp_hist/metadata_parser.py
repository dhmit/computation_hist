import os
import csv
import sqlite3
from pathlib import Path
from .models import *
from django.db import IntegrityError
from django.core.exceptions import ValidationError
from .common import DJWEB_PATH


def populate_from_metadata(file_name=None):
    '''
    :param file_name: is a path to a csv file (relative or actual)
    :return: populates the django database, but returns nothing
    how to run:
    open up terminal (with virtual environment):
    > cd djweb
    > python manage.py shell
    in shell:
    > from dj_comp_hist.metadata_parser import populate_from_metadata
    > populate_from_metadata()
    The 'r' in front of the file location isn't necessary but can help to prevent strange errors.
    Utilizes interpret_organization_person to add authors, recipients, and cced.
    '''

    if file_name is None:
        file_name = Path(os.path.abspath(os.path.dirname(__file__)), 'metadata.csv')

    with open(file_name) as file:
        csv_file = csv.DictReader(file)
        count_added = 0
        count_skipped = 0
        count_invalid = 0
        for line_id, line in enumerate(csv_file):
            # Skip empty lines
            if "".join(line.values()) == '':
                continue

            document_metadata_complete = True
            for attr in ['box', 'folder_number', 'doc_id', 'filename', 'author', 'title',
                         'first_page', 'last_page']:
                if not line[attr]:
                    print(f'WARNING: Line {line_id+1} is incomplete. Line {line}.')
                    document_metadata_complete = False
                    count_skipped += 1
                    break
            if document_metadata_complete:
                try:
                    add_one_document(line)
                    count_added += 1
                except ValidationError as e:
                    count_invalid += 1
                    print(f'{e}. Line: {line}.')


    print(f'Added {count_added} documents from {file_name}. Skipped {count_skipped} documents '
          f'because of incomplete metadata. Invalid: {count_invalid}')

    db = sqlite3.connect(Path(DJWEB_PATH.parent, 'db.sqlite3'))
    cursor = db.cursor()
    cursor.execute('create virtual table doc_fts using FTS4(id, title, text);')
    cursor.execute('''INSERT INTO doc_fts(id, title, text) 
                                                SELECT id, title, text 
                                                FROM dj_comp_hist_document;''')
    db.commit()

def add_one_document(csv_line):
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
    :return:
    """

    number_of_pages = int(csv_line['last_page']) - int(csv_line['first_page']) + 1
    new_doc = Document(number_of_pages=number_of_pages,
                       title=csv_line['title'],
                       type=csv_line['doc_type'],
                       notes=csv_line['notes'],
                       first_page=csv_line['first_page'],  # should this be an int?
                       last_page=csv_line['last_page'],
                       file_name=csv_line['filename']
                       )

    txt_path = get_file_path(box=int(csv_line['box']), folder=int(csv_line['folder_number']),
                             foldername_short=csv_line['foldername_short'],
                             doc_id=csv_line['doc_id'], path_type='absolute', file_type='txt')
    try:
        with open(txt_path, 'r', encoding='utf8') as f:
            new_doc.text = f.read()
    except FileNotFoundError:
        print(f'skipped {txt_path}')
        new_doc.text = ''

    # ---------------------DATE-----------------------------------------------
    if csv_line['date'] != '' and csv_line['date'][0] == '1':
        new_doc.date = csv_line['date']

    # ------------------------------------------------------------------------

    # ---------------------Folder---------------------------------------------
    folder_exist, new_folder = check_generate(Folder, "name", csv_line['foldername_short'])
    if not folder_exist:
        box_exist, new_box = check_generate(Box, "number", csv_line['box'])
        new_box.save()
        new_folder.box = new_box
        new_folder.number = csv_line['folder_number']
        new_folder.full = csv_line['foldername_full']
        new_folder.file_name = csv_line['filename']
    new_folder.save()
    new_doc.folder = new_folder


    # This would be better with create_or_update so that changed values get updated.
    # Not super important, though, as flushing the db will also update the values
    try:
        new_doc.save()
        # -----------------------Author, Recipient,cced--------------------------
        interpret_person_organization(csv_line['author'],
                                      "author_organization",
                                      "author_person",
                                      new_doc
                                      )
        interpret_person_organization(csv_line['recipients'],
                                      "recipient_organization",
                                      "recipient_person",
                                      new_doc
                                      )
        interpret_person_organization(csv_line['cced'],
                                      "cced_organization",
                                      "cced_person",
                                      new_doc
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
    return
