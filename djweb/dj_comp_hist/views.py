from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Person, Document, Box, Folder, Organization, Page
from django.template import loader, Context
from django.db.models import Q

# Create your views here.

from django.http import HttpResponse


def index(request):
    return render(request, 'index.jinja2')


def person(request, person_id):
    person_obj = get_object_or_404(Person, pk=person_id)
    document_written_objs = person_obj.author_person.all()
    document_received_objs = person_obj.recipient_person.all()
    document_cced_objs = person_obj.cced_person.all()
    x = render(request, 'person.jinja2', {'person_obj': person_obj, 'document_written_objs':
        document_written_objs, 'document_received_objs': document_received_objs, 'document_cced_objs': document_cced_objs})
    return x


def doc(request, doc_id):
    doc_obj = get_object_or_404(Document, pk=doc_id)
    author_person_objs = doc_obj.author_person.all()
    author_organization_objs = doc_obj.author_organization.all()
    recipient_person_objs = doc_obj.recipient_person.all()
    recipient_organization_objs = doc_obj.recipient_organization.all()
    cced_person_objs = doc_obj.cced_person.all()
    cced_organization_objs = doc_obj.cced_organization.all()
    page_objs = doc_obj.page_set.all()
    return render(request, 'doc.jinja2', {'doc_obj': doc_obj, 'author_person_objs':
        author_person_objs, 'author_organization_objs': author_organization_objs,
                                        'recipient_person_objs': recipient_person_objs,
                                        'recipient_orgaization_objs':
                                            recipient_organization_objs, 'cced_person_objs':
                                            cced_person_objs, 'cced_organization_objs':
                                              cced_organization_objs, 'page_objs': page_objs})


def box(request, box_id):
    box_obj = get_object_or_404(Box, pk=box_id)
    folder_objs = box_obj.folder_set.all()
    return render(request, 'box.jinja2', {'box_obj': box_obj, 'folder_objs': folder_objs})


def folder(request, folder_id):
    folder_obj = get_object_or_404(Folder, pk=folder_id)
    document_objs = folder_obj.document_set.all()
    response = render(request, 'folder.jinja2', {'folder_obj': folder_obj, 'document_objs':
        document_objs})
    return response


def organization(request, org_id):
    org_obj = get_object_or_404(Organization, pk=org_id)
    document_written_objs = org_obj.author_organization.all()
    document_received_objs = org_obj.recipient_organization.all()
    document_cced_objs = org_obj.cced_organization.all()
    response = render(request, 'organization.jinja2', {'org_obj': org_obj, 'document_written_objs':
        document_written_objs, 'document_received_objs': document_received_objs,
                                                       'document_cced_objs': document_cced_objs})
    return response


def page(request, page_id):
    page_obj = get_object_or_404(Page, pk=page_id)
    image_obj = page_obj.image_path
    document_obj = page_obj.document
    response = render(request, 'page.jinja2', {'page_obj': page_obj, 'image_obj': image_obj, 'document_obj':document_obj})
    return response

def list(request, model_str):
    if model_str == "organization":
        model = Organization
    elif model_str == "person":
        model = Person
    elif model_str == "folder":
        model = Folder
    elif model_str == "box":
        model = Box
    model_objs = get_list_or_404(model)
    response = render(request, 'list.jinja2', {'model_objs': model_objs, 'model_str': model_str})
    return response

def search(request):
    query = request.POST['usr_query']
    print("QUERY: ")
    print(query)
    t = loader.get_template('/earch.jinja2')
    c = {'query': query}

    return HttpResponse(t.render(c))

def search_results(request):
    """
    Searches database to check whether user input is contained within person's first/last name,
    document title, folder full name, organization name or location.

    :param request:
    :return:
    """
    #key

    user_input = request.GET['q']

    people_objs = Person.objects.filter(Q(last__contains=user_input) | Q(
        first__contains=user_input))
    document_objs = Document.objects.filter(title__contains=user_input)
    folder_objs = Folder.objects.filter(full__contains=user_input)
    organization_objs = Organization.objects.filter(Q(name__contains=user_input)|Q(
        location__contains=user_input))
    response = render(request, 'search_results.jinja2', {'people_objs': people_objs,
                                                         'document_objs': document_objs,
                                                         'folder_objs': folder_objs,
                                                         'organization_objs': organization_objs})
    return response


