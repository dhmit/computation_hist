from django.db import models

from utilities.common import get_file_path


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

    @property
    def url(self):
        return f'/archives/organization/{self.pk}'


class Person(models.Model):
    first = models.CharField(max_length=191, blank=True)
    last = models.CharField(max_length=191, blank=True)
    organization = models.ManyToManyField(Organization, blank=True)

    def __str__(self):
        if self.last and self.first:
            return self.last + ' ' + str(self.first)[0]
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
        return self.first + " " + self.last

    @property
    def url(self):
        return f'/archives/person/{self.pk}'


class Box(models.Model):
    number = models.IntegerField(default=0)

    def __str__(self):
        return str(self.number)

    def __repr__(self):
        return f"<Box {self.number}>"


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
    notes = models.TextField(blank=True)
    file_name = models.CharField(max_length=191, unique=True)
    text = models.TextField(blank=True)

    #  https://docs.djangoproject.com/en/2.1/ref/utils/#django.utils.text.slugify
    slug = models.SlugField(max_length=191, unique=True)

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

    @property
    def url(self):
        return f'/archives/doc/{self.slug}'

    def get_person_list(self, list_type):
        """
        :param list_type: 'authors', 'recipients', 'cceds'
        Returns a list of the names and urls of both person and organization
        authors/recipients/cceds
        Created because querysets that include both persons and organizations can't be merged.
        Currently used in the display of advanced search results. Could also be used in document
        display.
        """
        if list_type == 'authors':
            pl = [{'name': p.fullname, 'url': p.url} for p in self.author_person.all()]
            pl += [{'name': o.name, 'url': o.url} for o in self.author_organization.all()]
        elif list_type == 'recipients':
            pl = [{'name': p.fullname, 'url': p.url} for p in self.recipient_person.all()]
            pl += [{'name': o.name, 'url': o.url} for o in self.recipient_organization.all()]
        elif list_type == 'cceds':
            pl = [{'name': p.fullname, 'url': p.url} for p in self.cced_person.all()]
            pl += [{'name': o.name, 'url': o.url} for o in self.cced_organization.all()]
        else:
            raise ValueError(f'''Document.get_person_list can only have "authors", "recipients" and
                                 cceds as params but not {list_type}.''')

        return pl


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
