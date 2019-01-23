from django.db import models
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


class Box(models.Model):
    number = models.IntegerField(default=0)

    def __str__(self):
        return str(self.number)


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


class Folder(models.Model):
    name = models.CharField(max_length=191)
    box = models.ForeignKey(Box, on_delete=models.CASCADE)
    full = models.CharField(max_length=191)
    number = models.IntegerField(default=0)

    def __str__(self):
        return self.full

    def __repr__(self):
        return 'Folder' + self.name + ' ' + self.number


class Document(models.Model):
    author_person = models.ManyToManyField(Person, related_name='author_person', blank=True)
    author_organization = models.ManyToManyField(Organization,
                                                 related_name='author_organization', blank=True)
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE)
    title = models.CharField(max_length=191)
    type = models.CharField(max_length=191, blank=True)
    # TODO: turn type into choices- note that choices needs to be able to grow
    number_of_pages = models.IntegerField(default=1)
    date = models.DateField(auto_now_add=False, auto_now=False, blank=True)
    recipient_person = models.ManyToManyField(Person, related_name='recipient_person', blank=True)
    recipient_organization = models.ManyToManyField(Organization,
                                                    related_name='recipient_organization',
                                                    blank=True)

    def __str__(self):
        if self.title:
            return self.title
        else:
            return "No title"


class Page(models.Model):
    document = models.ForeignKey(Document, on_delete=models.CASCADE)
    page_number = models.IntegerField(default=0)
    file_name = models.CharField(max_length=191)

    def __str__(self):
        return "Page " + str(self.page_number) + " of " + str(self.document)


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


def populate_from_metadata(file_name):
    with open(file_name) as file:
        csv_file = csv.DictReader(file)
        for line in csv_file:
            new_doc = Document(number_of_pages=int(line['last_page']) - int(line['first_page']) + 1,
                               title=line['title'],
                               type=line['doc_type'])

            # ---------------------DATE-----------------------------------------------
            if line['date'] == '' or line['date'][0] != '1':
                new_doc.date = '1900-01-01'
            else:
                new_doc.date = line['date']

            # ------------------------------------------------------------------------

            # ---------------------Folder-----------------------------------------------
            folder_exist,new_folder = check_generate(Folder, "name" ,line['foldername_short'])
            if not folder_exist:
                box_exist,new_box = check_generate(Box, "number" , line['box'])
                new_box.save()
                new_folder.box = new_box
                new_folder.full = line['foldername_full']
            new_folder.save()
            new_doc.folder = new_folder

            # ------------------------------------------------------------------------


            # -----------------------Author--------------------------------------------

            #Creates list of authors
            auth_split = line['author'].split('; ')
            #Checks if it is an organization
            if len(auth_split) == 1 and len(auth_split[0].split(', ')) == 1:
                org_exist,new_org = check_generate(Organization, "name", auth_split[0])
                if not org_exist:
                    new_org.save()
                new_doc.author_organization.add(new_org)
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

            new_doc.save()


    return