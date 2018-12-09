from django.shortcuts import render, get_object_or_404
from .models import Person


# Create your views here.

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at Computation History project.")


def person(request, person_id):
    person_obj = get_object_or_404(Person, pk=person_id)
    # response = f"You're looking at {person_obj.first} {person_obj.last}"
    return render(request, 'person.html', {'person_obj': person_obj})
    # return HttpResponse(response)



def document(request, document_id):
    pass