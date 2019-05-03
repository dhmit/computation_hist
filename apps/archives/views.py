import random
import re

from django.db.models import Q
from django.http import Http404
from django.shortcuts import get_list_or_404, get_object_or_404, render
from django.template.loader import TemplateDoesNotExist
from django.core.exceptions import ObjectDoesNotExist

from utilities.common import get_file_path
from .models import Person, Document, Box, Folder, Organization


# NOTE(ra): this hardcoded pattern isn't great, but we're since we're using
# jinja2 templates as a data source for the stories, it gets us to a usable
# prototype without having to, e.g., read the folder of story templates
# and load their names dynamically. We'll replace this with something
# more robust once the story system takes firmer shape.

STORIES = [
    'announcement_of_the_IBM_704',
    'debugging',
    'mayowa_story',
    'qualifications_for_programmer',
    'time_records',
    'digital_humanities',
    'women_in_symbols',
]


def index(request):
    story_selection = random.sample(STORIES, 6)
    context = {'stories': story_selection}
    return render(request, 'index.jinja2', context)


def person(request, slug):
    person_obj = get_object_or_404(
        Person.objects.prefetch_related(
            'author_person',
            'recipient_person',
            'cced_person',
        ),
        slug=slug)
    document_written_objs = person_obj.author_person.all()
    document_received_objs = person_obj.recipient_person.all()
    document_cced_objs = person_obj.cced_person.all()
    obj_dict = {
        'person_obj': person_obj,
        'document_written_objs': document_written_objs,
        'document_received_objs': document_received_objs,
        'document_cced_objs': document_cced_objs
    }
    return render(request, 'archives/person.jinja2', obj_dict)


def doc(request, doc_id=None, slug=None):
    """
    Puts a document on the screen
    :param request:
    :param doc_id:
    :param slug:
    :return:
    """

    if doc_id:
        doc_obj = get_object_or_404(Document, pk=doc_id)
    elif slug:
        doc_obj = get_object_or_404(Document, slug=slug)
    else:
        # NOTE(ra): the case in which both slug and doc_id are both None
        # is unreachable (there's no url pattern matching them), so if you
        # reach this branch, something has gone awry.

        # TODO(ra): implement this branch
        # 1. add a url pattern that matches
        # 2. then do something sensible here... (probably a redirect)
        raise RuntimeError('This branch should be unreachable!')

    author_person_objs = doc_obj.author_person.all()
    author_organization_objs = doc_obj.author_organization.all()
    recipient_person_objs = doc_obj.recipient_person.all()
    recipient_organization_objs = doc_obj.recipient_organization.all()
    if recipient_organization_objs:
        if recipient_organization_objs[0].name == 'unknown':
            recipient_organization_objs = None
    cced_person_objs = doc_obj.cced_person.all()
    cced_organization_objs = doc_obj.cced_organization.all()
    if cced_organization_objs:
        if cced_organization_objs[0].name == 'unknown':
            cced_organization_objs = None
    doc_pdf_url = str(get_file_path(doc_obj.folder.box.number, doc_obj.folder.number,
                                    doc_obj.folder.name, file_type='pdf', path_type='aws',
                                    doc_id=doc_obj.doc_id))
    print(doc_pdf_url)
    print(doc_obj.date)
    obj_dict = {
        'doc_obj': doc_obj,
        'author_person_objs': author_person_objs,
        'author_organization_objs': author_organization_objs,
        'recipient_person_objs': recipient_person_objs,
        'recipient_organization_objs': recipient_organization_objs,
        'cced_person_objs': cced_person_objs,
        'cced_organization_objs': cced_organization_objs,
        'doc_pdf_url': doc_pdf_url,
    }
    return render(request, 'archives/doc.jinja2', obj_dict)


def box(request, slug):
    box_obj = get_object_or_404(Box, slug=slug)
    folder_objs = box_obj.folder_set.all()
    obj_dict = {
        'box_obj': box_obj,
        'folder_objs': folder_objs
    }
    return render(request, 'archives/box.jinja2', obj_dict)


def folder(request, slug):
    folder_obj = get_object_or_404(Folder, slug=slug)
    document_objs = folder_obj.document_set.all()
    obj_dict = {
        'folder_obj': folder_obj,
        'document_objs': document_objs
    }
    response = render(request, 'archives/folder.jinja2', obj_dict)

    return response


def organization(request, slug):
    org_obj = get_object_or_404(Organization, slug=slug)
    document_written_objs = org_obj.author_organization.all()
    document_received_objs = org_obj.recipient_organization.all()
    document_cced_objs = org_obj.cced_organization.all()
    obj_dict = {
        'org_obj': org_obj,
        'document_written_objs': document_written_objs,
        'document_received_objs': document_received_objs,
        'document_cced_objs': document_cced_objs
    }
    response = render(request, 'archives/organization.jinja2', obj_dict)
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
    elif model_str == "person":
        model_objs = get_list_or_404(Person)
    elif model_str == "folder":
        model_objs = get_list_or_404(Folder)
    elif model_str == "box":
        model_objs = get_list_or_404(Box)
    else:
        raise ValueError("Cannot display this model. Can only display organization, person, "
                         "folder, or box")
    obj_dict = {
        'model_objs': model_objs,
        'model_str': model_str,
    }
    response = render(request, 'archives/list.jinja2', obj_dict)
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
    people_objs = Person.objects.filter(Q(last__icontains=user_input) |
                                        Q(first__icontains=user_input))
    document_objs = Document.objects.filter(title__icontains=user_input)
    folder_objs = Folder.objects.filter(full__icontains=user_input)
    organization_objs = Organization.objects.filter(Q(name__icontains=user_input) |
                                                    Q(location__icontains=user_input))


    obj_dict = {
        'people_objs': people_objs,
        'document_objs': document_objs,
        'folder_objs': folder_objs,
        'organization_objs': organization_objs,
        'query': user_input,
    }
    response = render(request, 'archives/search_results.jinja2', obj_dict)
    return response


def browse(request):
    return render(request, 'archives/browse.jinja2')


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
        return render(request, 'archives/advanced_search.jinja2', {'doc_types': doc_types})

    results = process_advanced_search(search_params)
    search_objs = {
        'results': results,  # = doc_objs
        'search_params': search_params,
        'doc_types': doc_types
    }
    return render(request, 'archives/advanced_search.jinja2', search_objs)


def process_advanced_search(search_params):
    """
    Processes one advanced search request and returns the search_results as a queryset

    :param search_params:
    :return:
    """

    docs_qs = Document.objects  # 'qs' for queryset
    keywords = search_params.get('keyword')
    if keywords:
        keywordlst = keywords.split(" ")
        person_q = Q()
        for word in keywordlst:
            person_q |= Q(first__iexact=word)
            person_q |= Q(last__iexact=word)
        people_objs = Person.objects.filter(person_q)
        folder_objs = Folder.objects.filter(full__icontains=keywords)
        organization_objs = Organization.objects.filter(Q(name__icontains=keywords))
        doc_Q = Q(title__icontains=keywords)
        for person in people_objs:
            doc_Q |= Q(author_person=person)
            doc_Q |= Q(recipient_person=person)
        for org in organization_objs:
            doc_Q |= Q(author_organization=org)
            doc_Q |= Q(recipient_organization=org)
        for folder in folder_objs:
            doc_Q |= Q(folder=folder)
        docs_qs = docs_qs.filter(doc_Q)

    title = search_params.get('title')
    if title:
        docs_qs = docs_qs.filter(Q(title__icontains=title))

    text = search_params.get('text')  # full text search
    if text:
        words_q = Q()

        # handle exact search terms wrapped in " or '
        exact_searches = re.findall(r'"([^"]+)"', text)
        if exact_searches:
            for phrase in exact_searches:
                print(phrase)
                words_q &= Q(text__icontains=phrase)
                text = re.sub(phrase, '', text) # strip exact search search terms out

        # handle all leftover text
        text = re.sub(r'[\'"]', '', text)
        words = text.split()
        for word in words:
            words_q &= Q(text__icontains=word)
        docs_qs = docs_qs.filter(words_q)

    author = search_params.get('author')
    if author:
        author_names = author.split(" ")
        author_q = Q()
        for name in author_names:
            author_q |= Q(author_person__first__icontains=name)
            author_q |= Q(author_person__last__icontains=name)
            author_q |= Q(author_organization__name__icontains=name)
        docs_qs = docs_qs.filter(author_q)

    recipient = search_params.get('recipient')
    if recipient:
        recipient_names = recipient.split(" ")
        recipient_q = Q()
        for name in recipient_names:
            recipient_q |= Q(recipient_person__first__icontains=name)
            recipient_q |= Q(recipient_person__last__icontains=name)
            recipient_q |= Q(recipient_organization__name__icontains=name)
        docs_qs = docs_qs.filter(recipient_q)

    doc_types = search_params.getlist('doc_type')
    # if a key points to a list of values, querydict.get() just returns the last item in the list!
    # https://docs.djangoproject.com/en/2.1/ref/request-response/#django.http.QueryDict.__getitem__
    if doc_types:
        docs_qs = docs_qs.filter(type__in=doc_types)

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

    # prevents template from hitting the db
    docs_qs = docs_qs.prefetch_related('author_person', 'author_organization', 'folder',
                                       'recipient_person', 'recipient_organization')

    return docs_qs


def story(request, slug):
    if not slug in STORIES:
        raise Http404('A story with this slug does not exist.')

    template = f'archives/stories/{slug}.jinja2'
    return render(request, template)


def net_viz(request):
    import json
    from pathlib import Path

    network = Path('static', 'json', 'network.json')
    with open(network, 'r') as file:
        graph = file.read()

    graph_dict = json.loads(graph)

    nodes = graph_dict['nodes']
    links = graph_dict['links']

    # Sorts out everything but the top 100 nodes
    nodes = sorted(nodes, key=lambda i: i['weight'], reverse=True)[:100]
    node_list = [i['id'] for i in nodes]

    # Removes all links that connect to nodes that no longer exist
    links = [i for i in links if i['source'] in node_list and i['target'] in node_list]

    graph_dict = {'nodes': nodes, 'links': links}
    return render(request, 'archives/net_viz.jinja2', graph_dict)

    
def stories(request):
    template = 'archives/stories.jinja2'
    context = {'stories': STORIES}
    return render(request, template, context)

