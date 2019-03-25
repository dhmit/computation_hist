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
    search_params = request.GET
    if not search_params:
        return render(request, 'advanced_search.jinja2', {'doc_types': doc_types})

    results = process_advanced_search(search_params)
    search_objs = {
        'results': results,  # = doc_objs
        'search_params': search_params,
        'doc_types': doc_types
    }
    return render(request, 'advanced_search.jinja2', search_objs)


def process_advanced_search(search_params):
    """
    Processes one advanced search request and returns the search_results as a queryset

    :param request:
    :return:
    """

    docs_qs = Document.objects # 'qs' for queryset
 
    title = search_params.get('title')
    if title:
        docs_qs = docs_qs.filter(Q(title__icontains=title))

    text = search_params.get('text')
    if text:
        # allows quotation marks but only extracts the string in the middle
        match = re.match('^[\'\"]?([a-zA-Z\d ]+)[\'\"]?$', text)
        if not match:
            print(f"WARNING. Could not parse full text search string: {text}.")
        else:
            raw_docs = Document.objects.raw(f'''SELECT * FROM doc_fts 
                                                     WHERE text MATCH "{match.groups()[0]}";''')
            doc_ids = [doc.id for doc in raw_docs]
            docs_qs = docs_qs.filter(id__in=doc_ids)

    author = search_params.get('author')
    if author:
        author_names = author.split(" ")
        docs_qs = docs_qs.filter(Q(author_person__first__icontains=author_names[0]) |
                                   Q(author_person__last__icontains=author_names[0]) |
                                   Q(author_organization__name__icontains=author_names[0]))

    recipient = search_params.get('recipient')
    if recipient:
        recipient_names = recipient.split(" ")
        docs_qs = docs_qs.filter(Q(recipient_person__first__icontains=recipient_names[0]) |
                                   Q(recipient_person__last__icontains=recipient_names[0]) |
                                   Q(recipient_organization__name__icontains=recipient_names[0]))

    doc_types = search_params.getlist('doc_type')
    # if a key points to a list of values, querydict.get() just returns the last item in the list!
    # see: https://docs.djangoproject.com/en/2.1/ref/request-response/#django.http.QueryDict.__getitem__
    if doc_types:
        docs_qs.filter(type__in=doc_types)

    min_year = search_params.get('min_year')
    max_year = search_params.get('max_year')
    if min_year == '':
        min_year = 1900
    if max_year == '':
        max_year = 2000
    if min_year and max_year:
        # TODO: this will break if we can't cast these to int - fine for now
        # bc we validate in the frontend
        min_year = int(min_year)
        max_year = int(max_year)
        docs_qs = docs_qs.filter(Q(date__year__gte=min_year) &
                                 Q(date__year__lte=max_year))


    return docs_qs
