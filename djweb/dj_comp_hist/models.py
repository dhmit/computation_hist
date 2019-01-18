from django.db import models
import csv

# Create your models here.


class Organization(models.Model):
    location = models.CharField(max_length=191, blank=True)


class Box(models.Model):
    number = models.IntegerField(default=0)


class Person(models.Model):
    first = models.CharField(max_length=191, blank=True)
    last = models.CharField(max_length=191, blank=True)
    organization = models.ManyToManyField(Organization, blank=True)

    def __str__(self):
        if self.last and self.first:
            return self.last + ' ' + self.first[0]
        elif self.last :
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


class Document(models.Model):
    author_person = models.ManyToManyField(Person, related_name='author_person', blank=True)
    author_organization = models.ManyToManyField(Organization,
                                                 related_name='author_organization', blank=True)
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE)
    title = models.CharField(max_length=191, blank=True)
    type = models.CharField(max_length = 191, blank=True)
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


class Text(models.Model):
    page = models.OneToOneField(Page, on_delete=models.SET(None))

def populate_from_metadata(file_name):
    with open(file_name) as file:
        csv_file = csv.DictReader(file)
        i=0
        for line in csv_file:
            i += 1
            print(i)
            new_doc = Document(number_of_pages=int(line['last_page']) - int(line['first_page']) + 1,
                               title=line['title'],
                               type=line['doc_type'])
            if line['date'] != '' and line['date'][0] != '1':
                new_doc.date = '1900-01-01'
            else:
                new_doc.date = line['date']
            filter_folder = Folder.objects.filter(name=line['foldername_short'])
            print(filter_folder)
            print(line['foldername_short'])
            if Folder.objects.filter(name=line['foldername_short']):
                new_doc.Folder = line['foldername_short']
    return