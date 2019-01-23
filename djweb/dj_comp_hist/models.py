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
    date = models.DateField(auto_now_add=False, auto_now=False, blank=True)
    recipient_person = models.ManyToManyField(Person, related_name='recipient_person', blank=True)
    recipient_organization = models.ManyToManyField(Organization,
                                                    related_name='recipient_organization',
                                                    blank=True)
    cced_person = models.ManyToManyField(Person, related_name='cced_person', blank=True)
    cced_organization = models.ManyToManyField(Organization, related_name='cced_organization',
                                               blank=True)
    notes = models.CharField(max_length=191, blank=True)

    def __str__(self):
        return self.title

    def __repr__(self):
        return f"<Document {self.title}>"


class Page(models.Model):
    document = models.ForeignKey(Document, on_delete=models.CASCADE)
    page_number = models.IntegerField(default=0)
    file_name = models.CharField(max_length=191)

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


def populate_from_metadata(file_name):
    with open(file_name) as file:
        csv_file = csv.DictReader(file)
        for line in csv_file:
            new_doc = Document(number_of_pages=int(line['last_page']) - int(line['first_page']) + 1,
                               title=line['title'], type=line['doc_type'], notes=line['notes'])

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