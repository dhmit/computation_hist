from django.db import models

# Create your models here.

class Person(models.Model):
    first = models.CharField(max_length=191)
    last = models.CharField(max_length=191)

class Document(models.Model):
    author = models.ForeignKey(Person, on_delete=models.CASCADE)
    title = models.CharField(max_length=191)
    filename = models.CharField(max_length=191)

