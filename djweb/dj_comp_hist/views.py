from django.shortcuts import render, get_object_or_404
from .models import Person, Document


# Create your views here.

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at Computation History project.")


def person(request, person_id):
    person_obj = get_object_or_404(Person, pk=person_id)
    document_objs = person_obj.author.all()


    x = render(request, 'person.html', {'person_obj': person_obj, 'document_objs': document_objs,
                                        'length': len(document_objs)})
    print("******************")
    print(Document)

    return x



def doc(request, doc_id):
    doc_obj = get_object_or_404(Document, pk=doc_id)
    response = f"You're looking at {doc_obj.title} by {doc_obj.author.first().first} {doc_obj.author.first().last}"
    # return render(request, 'doc.html', {'doc_obj': person_obj})
    return HttpResponse(response)



def document(request, document_id):
    pass