from django.db import models

class Organization(models.Model):
    location = models.CharField(max_length=191, blank=True)
    name = models.CharField(max_length=191, blank=True)
    slug = models.SlugField(max_length=191, unique=True)

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
        return f'/archives/organization/{self.slug}'

    class Meta:
        ordering = ['name']


class Person(models.Model):
    first = models.CharField(max_length=191, blank=True)
    last = models.CharField(max_length=191, blank=True)
    organization = models.ManyToManyField(Organization, blank=True)
    slug = models.SlugField(max_length=191, unique=True)

    def __str__(self):
        if self.last and self.first:
            return self.last + ', ' + self.first
        elif self.last:
            return self.last + ', [first name unknown]'
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
        if self.last and self.first:
            return self.first + " " + self.last
        elif self.last:
            return '[first name unknown] ' + self.last
        elif self.first:
            return self.first + ' [last name unknown]'
        else:
            return "No name"

    @property
    def url(self):
        return f'/archives/person/{self.slug}'

    class Meta:
        ordering = ['last', 'first']


class Box(models.Model):
    number = models.IntegerField(default=0)
    slug = models.SlugField(max_length=191, unique=True)


    def __str__(self):
        return str(self.number)

    def __repr__(self):
        return f"<Box {self.number}>"

    @property
    def url(self):
        return f'/archives/box/{self.slug}'

    class Meta:
        ordering = ['number']


class Folder(models.Model):
    name = models.CharField(max_length=191)
    box = models.ForeignKey(Box, on_delete=models.CASCADE)
    full = models.CharField(max_length=191)
    number = models.IntegerField(default=0)
    slug = models.SlugField(max_length=191, unique=True)

    def __str__(self):
        return self.full

    def __repr__(self):
        return f"<Folder {self.full} - {self.number}>"

    @property
    def url(self):
        return f'/archives/folder/{self.slug}'

    class Meta:
        ordering = ['box__number', 'number', 'full']


class Document(models.Model):
    title = models.CharField(max_length=191)
    file_name = models.CharField(max_length=191, unique=True)
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE)
    doc_id = models.IntegerField() # sequence in the folder
    type = models.CharField(max_length=191, blank=True) # TODO: turn type into choices- note that choices needs to be able to grow
    number_of_pages = models.IntegerField(default=1)
    first_page = models.IntegerField(default=0)
    last_page = models.IntegerField(default=0)
    date = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)

    author_person = models.ManyToManyField(Person, related_name='author_person', blank=True)
    author_organization = models.ManyToManyField(Organization,
                                                 related_name='author_organization', blank=True)
    recipient_person = models.ManyToManyField(Person, related_name='recipient_person', blank=True)
    recipient_organization = models.ManyToManyField(Organization,
                                                    related_name='recipient_organization',
                                                    blank=True)
    cced_person = models.ManyToManyField(Person, related_name='cced_person', blank=True)
    cced_organization = models.ManyToManyField(Organization, related_name='cced_organization',
                                               blank=True)

    notes = models.TextField(blank=True)
    text = models.TextField(blank=True)

    #  https://docs.djangoproject.com/en/2.1/ref/utils/#django.utils.text.slugify
    slug = models.SlugField(max_length=191, unique=True)

    def __str__(self):
        return self.title

    def __repr__(self):
        return f"<Document {self.title}>"

    @property
    def citation(self):
        """ return a properly formatted citation as a string of HTML
            TODO: handle authors and date correctly
            see format at: https://dal.ca.libguides.com/archivalresearch/citation/APA 
        """
        cite = f'<i>{self.title}</i>. Records of the Massachusetts Institute of Technology Computation Center (AC.0062, Box {self.folder.box.number}, Folder {self.folder.number}). MIT Libraries Department of Distinctive Collections, Massachusetts Institute of Technology."'
        return cite

    @property
    def url(self):
        return f'/archives/doc/{self.slug}'

    @property
    def pdf_url(self):
        """ The url of the pdf on our AWS S3 bucket """
        base_url = 'https://s3.amazonaws.com/comp-hist/docs/'
        folder = f'{self.folder.box.number}_{self.folder.number}_{self.folder.name}'
        pdf_url = base_url + folder + '/docs/' + str(self.doc_id) + '/' + self.file_name + '.pdf'
        return pdf_url

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

    class Meta:
        ordering = ['doc_id']
