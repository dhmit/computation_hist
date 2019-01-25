from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Person, Document, Box, Folder, Organization

# Create your views here.

from django.http import HttpResponse


def index(request):
    return render(request, 'index.jinja2')


def person(request, person_id):
    person_obj = get_object_or_404(Person, pk=person_id)
    document_written_objs = person_obj.author_person.all()
    document_received_objs = person_obj.recipient_person.all()
    x = render(request, 'person.jinja2', {'person_obj': person_obj, 'document_written_objs':
        document_written_objs, 'document_received_objs': document_received_objs,})
    return x


def doc(request, doc_id):
    doc_obj = get_object_or_404(Document, pk=doc_id)
    response = f"You're looking at {doc_obj.title} by {doc_obj.author_person.first().first} {doc_obj.author_person.first().last}"
    # return render(request, 'doc.jinja2', {'doc_obj': person_obj})
    return HttpResponse(response)


def box(request, box_id):
    box_obj = get_object_or_404(Box, pk=box_id)
    folder_objs = box_obj.folder_set.all()
    return render(request, 'box.jinja2', {'box_obj': box_obj, 'folder_objs': folder_objs, 'length': len(folder_objs)})


def folder(request, folder_id):
    folder_obj = get_object_or_404(Folder, pk=folder_id)
    document_objs = folder_obj.document_set.all()
    response = render(request, 'folder.jinja2', {'folder_obj': folder_obj, 'document_objs':
        document_objs})
    return response


def organization(request, org_id):
    org_obj = get_object_or_404(Organization, pk=org_id)
    document_objs = org_obj.author_organization.all()
    response = render(request, 'organization.jinja2', {'org_obj': org_obj, 'document_objs':
        document_objs})
    return response


def list(request, model_str):
    if model_str == "organization":
        model = Organization
        print('model is',model)
    elif model_str == "person":
        model = Person
        print('model is', model)
    elif model_str == "folder":
        model = Folder
        print('model is', model)
    else:
        model = "404"
    model_objs = get_list_or_404(model)
    response = render(request, 'list.jinja2', {'model_objs': model_objs, 'model_str': model_str})
    return response