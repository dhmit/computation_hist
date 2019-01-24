from django.shortcuts import render, get_object_or_404
from .models import Person, Document, Box

# Create your views here.

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at Computation History project.")


def person(request, person_id):
    person_obj = get_object_or_404(Person, pk=person_id)
    document_objs = person_obj.author_person.all()
    x = render(request, 'person.html', {'person_obj': person_obj, 'document_objs': document_objs, 'length': len(document_objs)})
    return x


def doc(request, doc_id):
    doc_obj = get_object_or_404(Document, pk=doc_id)
    response = f"You're looking at {doc_obj.title} by {doc_obj.author_person.first().first} {doc_obj.author_person.first().last}"
    # return render(request, 'doc.html', {'doc_obj': person_obj})
    return HttpResponse(response)


def box(request, box_id):
    box_obj = get_object_or_404(Box, pk=box_id)
    folder_objs = box_obj.folder_set.all()
    return render(request, 'box.html', {'box_obj': box_obj, 'folder_objs': folder_objs, 'length': len(folder_objs)})

