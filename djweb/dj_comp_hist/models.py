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
                                 path_type='aws')
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
    # Adds people and organizations as an author, recipient, or CC'ed. Utilizes check_generate to
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

