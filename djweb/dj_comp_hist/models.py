from django.db import models
from django.db.models.signals import post_save
from django.db.models.signals import  post_save
from pdf2image import convert_from_path
import csv

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


class Page(models.Model):
    document = models.ForeignKey(Document, on_delete=models.CASCADE)
    page_number = models.IntegerField(default=0)
    image_path = models.CharField(max_length=191)

    def __str__(self):
        return "Page " + str(self.page_number) + " of " + str(self.document)

    def __repr__(self):
        return f"<Page {self.page_number} of {self.document}"


class Text(models.Model):
    page = models.OneToOneField(Page, on_delete=models.SET(None), blank=True)


def check_generate(model, key, value):
    if model.objects.filter(**{key: value}):
        existed = True
        new_item = model.objects.get(**{key: value})

    else:
        new_item = model(**{key: value})
        existed = False
    return existed, new_item

def check_person_known(person):
    if person.first == "unknown":
        person.first = ""
    if person.last == "unknown":
        person.last = ""
    return person


def interpret_person_organization(field, item_organization, item_person, new_doc):
    #Creates list of authors
    field_split = field.split('; ')
    #Checks if it is an organization

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


def populate_from_metadata(file_name):
    with open(file_name) as file:
        csv_file = csv.DictReader(file)
        for line in csv_file:
            new_doc = Document(number_of_pages=int(line['last_page']) - int(line['first_page']) + 1,
                               title=line['title'], type=line['doc_type'], notes=line['notes'],
                               first_page=line['first_page'], last_page=line['last_page'],
                               file_name=line['filename'])

            # ---------------------DATE-----------------------------------------------
            if line['date'] != '' and line['date'][0] == '1':
                new_doc.date = line['date']

            # ------------------------------------------------------------------------

            # ---------------------Folder---------------------------------------------
            folder_exist,new_folder = check_generate(Folder, "name" ,line['foldername_short'])
            if not folder_exist:
                box_exist,new_box = check_generate(Box, "number" , line['box'])
                new_box.save()
                new_folder.box = new_box
                new_folder.number = line['folder_number']
                new_folder.full = line['foldername_full']
                new_folder.file_name = line['filename']
            new_folder.save()
            new_doc.folder = new_folder
            new_doc.save()

            # -----------------------Author, Recipient,cced--------------------------
            interpret_person_organization(line['author'], "author_organization", "author_person", new_doc)
            interpret_person_organization(line['recipients'], "recipient_organization",
                                          "recipient_person",
                                          new_doc)
            interpret_person_organization(line['cced'], "cced_organization", "cced_person",
                                          new_doc)


            # -----------------------Author--------------------------------------------

            #Creates list of authors
            auth_split = line['author'].split('; ')
            #Checks if it is an organization
            if len(auth_split) == 1 and len(auth_split[0].split(', ')) == 1:
                org_exist,new_org = check_generate(Organization, "name", auth_split[0])
                if not org_exist:
                    new_org.save()
                new_org.save()
                new_doc.author_organization.add(Organization.objects.get(name=auth_split[0]))
            else:
                for auth in range(len(auth_split)):
                    auth_current = auth_split[auth].split(', ')
                    auth_exist,new_auth = check_generate(Person, "last", auth_current[0])
                    #TODO change check_generate to have more than one key for people with the
                    #same last name
                    if not auth_exist:
                        new_auth.first = auth_current[1]
                        new_auth.save()
                    new_doc.author_person.add(new_auth)
                    # same last name
                    if not auth_exist:
                        new_auth.first = auth_current[1]
                    new_auth.save()
                    new_doc.author_person.add(Person.objects.get(last=auth_current[0]))


            # -----------------------Recipient----------------------------------------

            recp_split = line['recipients'].split('; ')
            for recp in range(len(recp_split)):
                recp_current = recp_split[recp].split(', ')
                if '/' in recp_current[0]:
                    #TODO make if statement more specific to find organizations
                    recp_exist,new_recp = check_generate(Organization, "name", recp)
                    new_recp.save()
                    new_doc.recipient_organization.add(Organization.objects.get(name=recp))
                else:
                    recp_exist,new_recp = check_generate(Person, "last", recp_current[0])
                    if not recp_exist:
                        new_recp.first = recp_current[1]
                    new_recp.save()
                    new_doc.recipient_person.add(Person.objects.get(last=recp_current[0]))

            #-------------------------cced-------------------------------------------

            cced_split = line['cced'].split('; ')
            for cced in range(len(cced_split)):
                cced_current = cced_split[cced].split(', ')
                if '/' in cced_current[0]:
                    #TODO make if statement more specific to find organizations
                    cced_exist,new_cced = check_generate(Organization, "name", cced)
                    new_cced.save()
                    new_doc.recipient_organization.add(Organization.objects.get(name=cced))
                else:
                    cced_exist,new_cced = check_generate(Person, "last", cced_current[0])
                    if not cced_exist:
                        new_cced.first = cced_current[1]
                    new_cced.save()
                    new_doc.recipient_person.add(Person.objects.get(last=cced_current[0]))

            new_doc.save()

        return
"""
@reciever(post_save, sender=Document)

def create_pages(sender, instance, created, **kwargs):
    for i in range(1, instance.number_of_pages + 1):
        new_page = Page(document=instance, file_name=line['filename'], page_number=i)
        new_page.save(

"""


def pdf_to_image_split(pdf_path, image_directory, folder_name):
    pages = convert_from_path(pdf_path)
    images_in_pdf = []

    for page in range(len(pages)):
        page_path = image_directory + folder_name + '_' + str(page + 1) + '.png'
        pages[page].save(page_path, 'PNG')
        images_in_pdf.append((page_path, page+1))

    return images_in_pdf


def page_image_to_doc(folder_name, pdf_path, image_directory):
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
            page_obj = Page(document=documents_sort[document_place], page_number=page_num,
                            image_path=page[0])
            page_obj.save()
            page_num += 1
        elif documents_sort[document_place+1].first_page <= page[1] <= documents_sort[\
                document_place+1].last_page:
            # this means this is a new document
            document_place += 1
            page_num = 1
            page_obj = Page(document=documents_sort[document_place], page_number=page_num,
                            image_path=page[0])
            page_obj.save()
            page_num += 1
        else:
            # This means that the page isn't associated with a document
            pass
    return
