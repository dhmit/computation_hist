from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Person, Document, Box, Folder, Organization, Page
# from django.template import loader
from django.db.models import Q
from .common import get_file_path
from IPython import embed
import re



# from django.http import HttpResponse


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
    try:
        if recipient_organization_objs[0].name == 'unknown':
            recipient_organization_objs = None
    except:
        pass
    cced_person_objs = doc_obj.cced_person.all()
    cced_organization_objs = doc_obj.cced_organization.all()
    try:
        if cced_organization_objs[0].name == 'unknown':
            cced_organization_objs = None
    except:
        pass
    page_objs = doc_obj.page_set.all()
    doc_pdf_url = str(get_file_path(doc_obj.folder.box.number, doc_obj.folder.number,
                                    doc_obj.folder.name , file_type='pdf', path_type='aws',
                                    doc_id=doc_obj.doc_id))
    print(doc_pdf_url)
    print(doc_obj.date)
    obj_dict = {
        'doc_obj': doc_obj,
        'author_person_objs': author_person_objs,
        'author_organization_objs': author_organization_objs,
        'recipient_person_objs': recipient_person_objs,
        'recipient_orgaization_objs': recipient_organization_objs,
        'cced_person_objs': cced_person_objs,
        'cced_organization_objs': cced_organization_objs,
        'page_objs': page_objs,
        'doc_pdf_url': doc_pdf_url,
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
    """
    Displays sorted list of Organizations, People, Folders, or Boxes
    :param request:
    :param model_str:
    :return:
    """
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

    obj_dict = {
        'people_objs': people_objs,
        'document_objs': document_objs,
        'folder_objs': folder_objs,
        'organization_objs': organization_objs,
        'query': user_input,
    }
    response = render(request, 'search_results.jinja2', obj_dict)
    return response


def browse(request):
    return render(request, 'browse.jinja2')


def advanced_search(request):
    """
    Searches database based on specific search queries and parameters given by user.
    :param request:
    :return:
    """

    # Sorted list of all available document types
    doc_types = sorted(["minutes", "memo", "proposal", "letter", "receipt", "contract", "notice",
                        "memo draft", "addendum", "change order", "form", "report", "invoice",
                        "list", "routing sheet", "application", "note", "press release",
                        "floor plan", "program", "pamphlet", "payroll sheet", "time record",
                        "summary", "table", "telegram"])

    # if no search_params, that means we're just loading the search page
    if not request.GET.dict():
        return render(request, 'advanced_search.jinja2', {'doc_types': doc_types})
    else:
        search_params, results = process_advanced_search_request(request)
        search_objs = {
            'results': results,  # = doc_objs
            'search_params': search_params,
            'doc_types': doc_types
        }
        return render(request, 'advanced_search.jinja2', search_objs)


def process_advanced_search_request(request):
    """
    Processes one advanced search request and returns the search_results as a list of Document
    objects as well as the search_params as a dict.

    :param request:
    :return:
    """

    search_params = request.GET.dict()
    # doc_types param is a list but using request.GET['doc_type'] only returns the first one.
    search_params['doc_types'] = request.GET.getlist('doc_type')

    doc_objs = Document.objects

    if search_params['title'] != '':
        doc_objs = doc_objs.filter(Q(title__icontains=search_params['title']))

    if search_params['text'] != '':
        # allows quotation marks but only extracts the string in the middle
        match = re.match('^[\'\"]?([a-zA-Z\d ]+)[\'\"]?$', search_params['text'])
        if not match:
            print(f"WARNING. Could not parse full text search string: {search_params['text']}.")
        else:
            raw_docs = Document.objects.raw(f'''SELECT * FROM doc_fts 
                                                     WHERE text MATCH "{match.groups()[0]}";''')
            doc_ids = [doc.id for doc in raw_docs]
            doc_objs = doc_objs.filter(id__in=doc_ids)

    if search_params['author'] != '':
        author = search_params['author'].split(" ")
        doc_objs = doc_objs.filter(Q(author_person__first__icontains=author[0]) |
                                   Q(author_person__last__icontains=author[0]) |
                                   Q(author_organization__name__icontains=author[0]))

    if search_params['recipient'] != '':
        recipient = search_params['recipient'].split(" ")
        doc_objs = doc_objs.filter(Q(recipient_person__first__icontains=recipient[0]) |
                                   Q(recipient_person__last__icontains=recipient[0]) |
                                   Q(recipient_organization__name__icontains=recipient[0]))

    if search_params['doc_types']:
        doc_objs.filter(type__in=search_params['doc_types'])

    if search_params['min_year'] == '':
        search_params['min_year'] = 1900
    if search_params['max_year'] == '':
        search_params['max_year'] = 2000
    doc_objs = doc_objs.filter(Q(date__year__gte=int(search_params['min_year'])) &
                               Q(date__year__lte=int(search_params['max_year'])))


    return search_params, doc_objs
