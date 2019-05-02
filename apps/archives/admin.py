from django.contrib import admin

# Register your models here.

from .models import Person, Document, Organization, Box, Folder

admin.site.register(Person)
admin.site.register(Document)
admin.site.register(Organization)
admin.site.register(Box)
admin.site.register(Folder)

