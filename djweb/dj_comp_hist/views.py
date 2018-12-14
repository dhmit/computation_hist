from django.shortcuts import render, get_object_or_404
from .models import Person,Document
# Create your views here.

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at Computation History project.")

def person(request, person_id):
    person_obj = get_object_or_404(Person, pk=person_id)
    response = f"You're looking at {person_obj.first} {person_obj.last}"
    return HttpResponse(response)


def document(request,document_id):
    document_obj = get_object_or_404(Document, pk=document_id)
    response = f"This document, titled {document_obj.title} was made by {document_obj.author.first}"
    return HttpResponse(response)