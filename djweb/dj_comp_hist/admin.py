from django.contrib import admin

# Register your models here.

from .models import Person, Document

admin.site.register(Person)
admin.site.register(Document)

