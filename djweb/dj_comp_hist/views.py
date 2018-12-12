from django.shortcuts import render, get_object_or_404
from .models import Person, Document


# Create your views here.

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at Computation History project.")


def person(request, person_id):
    person_obj = get_object_or_404(Person, pk=person_id)
    response = f"You're looking at {person_obj.first} {person_obj.last}"
    # return render(request, 'person.html', {'person_obj': person_obj})
    return HttpResponse(response)

def doc(request, doc_id):
    doc_obj = get_object_or_404(Document, pk=doc_id)
    response = f"You're looking at {doc_obj.title} by {doc_obj.author.first} {doc_obj.author.last}"
    #return render(request, 'doc.html', {'doc_obj': person_obj})
    return HttpResponse(response)



def document(request, document_id):
    pass