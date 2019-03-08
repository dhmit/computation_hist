from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Person, Document, Box, Folder, Organization, Page
from django.template import loader
from django.db.models import Q
import json

# Create your views here.

from django.http import HttpResponse


def index(request):
    return render(request, 'index.jinja2')


def person(request, person_id):
    person_obj = get_object_or_404(Person, pk=person_id)
    document_written_objs = person_obj.author_person.all()
    document_received_objs = person_obj.recipient_person.all()
    document_cced_objs = person_obj.cced_person.all()
    obj_dict = {
        'person_obj': person_obj,
        'document_written_objs': document_written_objs,
        'document_received_objs': document_received_objs,
        'document_cced_objs': document_cced_objs
    }
    return render(request, 'person.jinja2', obj_dict)


def doc(request, doc_id):
    """
    Puts a document on the screen
    :param request:
    :param doc_id:
    :return:
    """
    doc_obj = get_object_or_404(Document, pk=doc_id)
    author_person_objs = doc_obj.author_person.all()
    author_organization_objs = doc_obj.author_organization.all()
    recipient_person_objs = doc_obj.recipient_person.all()
    recipient_organization_objs = doc_obj.recipient_organization.all()
    cced_person_objs = doc_obj.cced_person.all()
    cced_organization_objs = doc_obj.cced_organization.all()
    page_objs = doc_obj.page_set.all()
    obj_dict = {
        'doc_obj': doc_obj,
        'author_person_objs': author_person_objs,
        'author_organization_objs': author_organization_objs,
        'recipient_person_objs': recipient_person_objs,
        'recipient_orgaization_objs': recipient_organization_objs,
        'cced_person_objs': cced_person_objs,
        'cced_organization_objs': cced_organization_objs,
        'page_objs': page_objs
    }
    return render(request, 'doc.jinja2', obj_dict)


def box(request, box_id):
    box_obj = get_object_or_404(Box, pk=box_id)
    folder_objs = box_obj.folder_set.all()
    obj_dict = {
        'box_obj': box_obj,
        'folder_objs': folder_objs
    }
    return render(request, 'box.jinja2', obj_dict)


def folder(request, folder_id):
    folder_obj = get_object_or_404(Folder, pk=folder_id)
    document_objs = folder_obj.document_set.all()
    obj_dict = {
        'folder_obj': folder_obj,
        'document_objs': document_objs
    }
    response = render(request, 'folder.jinja2', obj_dict)
    return response


def organization(request, org_id):
    org_obj = get_object_or_404(Organization, pk=org_id)
    document_written_objs = org_obj.author_organization.all()
    document_received_objs = org_obj.recipient_organization.all()
    document_cced_objs = org_obj.cced_organization.all()
    obj_dict = {
        'org_obj': org_obj,
        'document_written_objs': document_written_objs,
        'document_received_objs': document_received_objs,
        'document_cced_objs': document_cced_objs
    }
    response = render(request, 'organization.jinja2', obj_dict)
    return response


def page(request, page_id):
    page_obj = get_object_or_404(Page, pk=page_id)
    document_obj = page_obj.document
    png_url_amz = page_obj.png_url
    try:
        next_page_number = page_obj.page_number + 1
        next_page = Page.objects.get(document=document_obj, page_number=next_page_number)
    except:  # TODO: figure out type of exception
        next_page = None
    try:
        previous_page_number = page_obj.page_number - 1
        previous_page = Page.objects.get(document=document_obj, page_number=previous_page_number)
    except:  # TODO: figure out type of exception
        previous_page = None
    obj_dict = {
        'page_obj': page_obj,
        'document_obj': document_obj,
        'next_page': next_page,
        'previous_page': previous_page,
        'png_url_amz': png_url_amz,
    }
    response = render(request, 'page.jinja2', obj_dict)
    return response


def list_obj(request, model_str):
    '''
    Displays sorted list of Organizations, People, Folders, or Boxes
    :param request:
    :param model_str:
    :return:
    '''
    if model_str == "organization":
        model_objs = get_list_or_404(Organization)
        model_objs.sort(key=lambda x: x.name)
    elif model_str == "person":
        model_objs = get_list_or_404(Person)
        model_objs.sort(key=lambda x: x.last)
    elif model_str == "folder":
        model_objs = get_list_or_404(Folder)
        model_objs.sort(key=lambda x: x.full)
    elif model_str == "box":
        model_objs = get_list_or_404(Box)
        model_objs.sort(key=lambda x: x.number)
    else:
        raise ValueError("Cannot display this model. Can only display organization, person, "
                         "folder, or box")
    obj_dict = {
        'model_objs': model_objs,
        'model_str': model_str,
    }
    response = render(request, 'list.jinja2', obj_dict)
    return response


def search_results(request):
    """
    Searches database to check whether user input is contained within person's first/last name,
    document title, folder full name, organization name or location.

    :param request:
    :return:
    """
    # key

    user_input = request.GET['q']

    people_objs = Person.objects.filter(Q(last__contains=user_input) | Q(
        first__contains=user_input))
    document_objs = Document.objects.filter(title__contains=user_input)
    folder_objs = Folder.objects.filter(full__contains=user_input)
    organization_objs = Organization.objects.filter(Q(name__contains=user_input)|Q(
        location__contains=user_input))

    doc_type = ["minutes","memo","proposal","letter","receipt","contract","notice","memo draft",
                "addendum","change order","form","report","invoice","list",
                "routing sheet","application","note","press release","floor plan","program",
                "pamphlet","payroll sheet","time record","summary","table","telegram"]

    doc_type.sort()
    obj_dict = {
        'doc_type': doc_type,
        'people_objs': people_objs,
        'document_objs': document_objs,
        'folder_objs': folder_objs,
        'organization_objs': organization_objs,
        'query': user_input,
    }
    response = render(request, 'search_results.jinja2', obj_dict)
    return response

def browse(request):
    return( render(request, 'browse.jinja2'))



def advanced_search(request):
    """
    Searches database based on specific search queries and parameters given by user.
    :param request:
    :return:
    """
    boxes = []
    if "checkBox1" in request.GET:
        boxes.append(1)
    if "checkBox2" in request.GET:
        boxes.append(2)
    if "checkBox3" in request.GET:
        boxes.append(3)
    if len(boxes) == 2:
        doc_objs = Document.objects.filter(Q(folder__box__number=boxes[0]) |
                                           Q(folder__box__number=boxes[1]))
    elif len(boxes) == 1:
        doc_objs = Document.objects.filter(folder__box__number=boxes[0])
    else:
        doc_objs = Document.objects
    try:
        author = request.GET['author']
        if author != "":
            author = author.split(" ")
            doc_objs = doc_objs.filter(Q(author_person__first__icontains=author[0]) |
                                       Q(author_person__last__icontains=author[0]) |
                                       Q(author_organization__name__icontains=author[0]))
    except:
        print("Error getting author name")
    try:
        recipient = request.GET['receiver']
        if recipient != "":
            recipient = recipient.split(" ")
            doc_objs = doc_objs.filter(Q(recipient_person__first__icontains=recipient[0]) |
                                       Q(recipient_person__last__icontains=recipient[0]) |
                                       Q(recipient_organization__name__icontains=recipient[0]))
    except:
        print('Error getting recipient name')
    try:
        doc_types = request.GET['doc_type'].split(',')
        print(doc_types)
        if isinstance(doc_types, list) and 'unknown' not in doc_types:
            queries = [Q(type__icontains=t) for t in doc_types]
            print(queries)
            query = queries.pop()
            for item in queries:
                query |= item
        elif doc_types != 'unknown':
            query = Q(type__icontains=doc_types)
        doc_objs = doc_objs.filter(query)
    except:
        print('Error getting doc types')
    try:
        pages = [int(request.GET['minPages']), int(request.GET['maxPages'])]
        doc_objs = doc_objs.filter(Q(number_of_pages__gte=pages[0]) &
                        Q(number_of_pages__lte=pages[1]))
    except:
        print('Error getting pages')

    try:
        years = [int(request.GET['minYear']), int(request.GET['maxYear'])]
        doc_objs = doc_objs.filter(Q(date__year__gte=years[0]) &
                                   Q(date__year__lte=years[1]))
    except:
        print('Error getting min and max years')

    print(request)

    return render(request,'list.jinja2', {'model_str': 'doc', 'model_objs': doc_objs})
