from django.db import models
# from django.db.models.signals import post_save
# from django.db.models.signals import  post_save
from pdf2image import convert_from_path
import csv
import os
from pathlib import Path
from .common import get_file_path

# Create your models here.


class Organization(models.Model):
    location = models.CharField(max_length=191, blank=True)
    name = models.CharField(max_length=191, blank=True)

    def __str__(self):
        if self.name:
            return self.name
        else:
            return "No name"

    def __repr__(self):
        if self.name:
            return f"<Organization {self.name}>"
        else:
            return f"<Organization without a name>"


class Box(models.Model):
    number = models.IntegerField(default=0)

    def __str__(self):
        return str(self.number)

    def __repr__(self):
        return f"<Box {self.number}>"


class Person(models.Model):
    first = models.CharField(max_length=191, blank=True)
    last = models.CharField(max_length=191, blank=True)
    organization = models.ManyToManyField(Organization, blank=True)

    def __str__(self):
        if self.last and self.first:

            return self.last + ' ' + self.first[0]

        elif self.last:
            return self.last
        elif self.first:
            return self.first
        else:
            return "No name"

    def __repr__(self):
        if self.last and self.first:
            return f"<Person {self.last}, {str(self.first)[0]}>"
        elif self.last:
            return f"<Person {self.last}>"
        elif self.first:
            return f"<Person {self.first}>"
        else:
            return f"<Person without a name>"

    @property
    def fullname(self):
        return self.first + "_" + self.last



class Folder(models.Model):
    name = models.CharField(max_length=191)
    box = models.ForeignKey(Box, on_delete=models.CASCADE)
    full = models.CharField(max_length=191)
    number = models.IntegerField(default=0)

    def __str__(self):
        return self.full

    def __repr__(self):
        return f"<Folder {self.full} - {self.number}>"


class Document(models.Model):
    author_person = models.ManyToManyField(Person, related_name='author_person', blank=True)
    author_organization = models.ManyToManyField(Organization,
                                                 related_name='author_organization', blank=True)
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE)
    title = models.CharField(max_length=191)
    type = models.CharField(max_length=191, blank=True)
    # TODO: turn type into choices- note that choices needs to be able to grow
    number_of_pages = models.IntegerField(default=1)
    first_page = models.IntegerField(default=0)
    last_page = models.IntegerField(default=0)
    date = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
    recipient_person = models.ManyToManyField(Person, related_name='recipient_person', blank=True)
    recipient_organization = models.ManyToManyField(Organization,
                                                    related_name='recipient_organization',
                                                    blank=True)
    cced_person = models.ManyToManyField(Person, related_name='cced_person', blank=True)
    cced_organization = models.ManyToManyField(Organization, related_name='cced_organization',
                                               blank=True)
    notes = models.CharField(max_length=191, blank=True)
    file_name = models.CharField(max_length=191, blank=True)

    def __str__(self):
        return self.title

    def __repr__(self):
        return f"<Document {self.title}>"

    @property
    def doc_id(self):
        id_num = []
        file = str(self.file_name)
        for char in reversed(range(len(file))):
            if file[char] != "_":
                id_num.append(file[char])
            else:
                break
        return int(''.join(reversed(id_num)))


class Page(models.Model):
    document = models.ForeignKey(Document, on_delete=models.CASCADE)
    page_number = models.IntegerField(default=0)

    def __str__(self):
        return "Page " + str(self.page_number) + " of " + str(self.document)

    def __repr__(self):
        return f"<Page {self.page_number} of {self.document}"

    @property
    def png_url(self):
        png_path = get_file_path(self.document.folder.box.number, self.document.folder.number,
                                 self.document.folder.name, file_type='png', 
                                 doc_id=self.document.doc_id, page_id=int(self.page_number),
                                 include_base_path=False, aws_file=True)
        return png_path

class Text(models.Model):
    page = models.OneToOneField(Page, on_delete=models.SET(None), blank=True)


def check_generate(model, key, value):
    # Checks if a certain object in a model exists and then generates it if it does not.
    if model.objects.filter(**{key: value}):
        existed = True
        new_item = model.objects.get(**{key: value})

    else:
        new_item = model(**{key: value})
        existed = False
    return existed, new_item


def check_person_known(person):
    # This function checks whether this person or organization has unknown apart of their name in
    # the metadata and the attributes that name to an empty string.
    if person.first == "unknown":
        person.first = ""
    if person.last == "unknown":
        person.last = ""
    return person


def interpret_person_organization(field, item_organization, item_person, new_doc):
    # Adds people and organizations as an author, recipient, or cced. Utilizes check_generata to
    # make the process easier.
    field_split = field.split('; ')

    for person_or_organization in field_split:
        if len(person_or_organization.split(', ')) == 1:
            org_exist, new_org = check_generate(Organization, "name", field_split[0])
            new_org.save()
            bound_attr = getattr(new_doc, item_organization)
            bound_attr.add(Organization.objects.get(name=field_split[0]))
        else:
            item_current = person_or_organization.split(', ')
            item_exist, new_item = check_generate(Person, "last", item_current[0])
            check_person_known(new_item)
            # TODO change check_generate to have more than one key for people with the
            # same last name
            if not item_exist:
                new_item.first = item_current[1]
            new_item.save()
            bound_attr = getattr(new_doc, item_person)
            bound_attr.add(new_item)


def populate_from_metadata(file_name=None):
    '''
    :param file_name: is a path to a csv file (relative or actual)
    :return: populates the django database, but returns nothing

    how to run:
    open up terminal (with virtual environment):
    > cd djweb
    > python manage.py shell

    in shell:
    > from dj_comp_hist.models import populate_from_metadata
    > populate_from_metadata()

    The 'r' in front of the file location isn't necessary but can help to prevent strange errors.
    Utilizes interpret_organization_person to add authors, recipients, and cced.
    '''

    if file_name is None:
        file_name = Path(os.path.abspath(os.path.dirname(__file__)), 'metadata_jan24.csv')

    with open(file_name) as file:
        csv_file = csv.DictReader(file)
        for line in csv_file:
            number_of_pages = int(line['last_page']) - int(line['first_page']) + 1
            new_doc = Document(number_of_pages=number_of_pages,
                               title=line['title'],
                               type=line['doc_type'],
                               notes=line['notes'],
                               first_page=line['first_page'],  # should this be an int?
                               last_page=line['last_page'],
                               file_name=line['filename']
                               )

            # ---------------------DATE-----------------------------------------------
            if line['date'] != '' and line['date'][0] == '1':
                new_doc.date = line['date']

            # ------------------------------------------------------------------------

            # ---------------------Folder---------------------------------------------
            folder_exist, new_folder = check_generate(Folder, "name", line['foldername_short'])
            if not folder_exist:
                box_exist, new_box = check_generate(Box, "number", line['box'])
                new_box.save()
                new_folder.box = new_box
                new_folder.number = line['folder_number']
                new_folder.full = line['foldername_full']
                new_folder.file_name = line['filename']
            new_folder.save()
            new_doc.folder = new_folder
            new_doc.save()

            # -----------------------Author, Recipient,cced--------------------------
            interpret_person_organization(line['author'],
                                          "author_organization",
                                          "author_person",
                                          new_doc
                                          )
            interpret_person_organization(line['recipients'],
                                          "recipient_organization",
                                          "recipient_person",
                                          new_doc
                                          )
            interpret_person_organization(line['cced'],
                                          "cced_organization",
                                          "cced_person",
                                          new_doc
                                          )

            new_doc.save()
        return


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
        images_in_pdf.append((page_path, page+1))

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
        if documents_sort[document_place].first_page <= page[1] <= documents_sort[\
                document_place].last_page:
            # this means that this is the same document as last page
            page_obj = Page(document=documents_sort[document_place], page_number=page_num)
            page_obj.image_path.name = folder_name + '_' + str(page[1]) + '.png'
            page_obj.save()
            page_num += 1
        elif documents_sort[document_place+1].first_page <= page[1] <= documents_sort[\
                document_place+1].last_page:
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


