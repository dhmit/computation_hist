import random

from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.shortcuts import get_object_or_404, render

from .models import Person, Document, Box, Folder, Organization
from .search import process_search
from utilities.common import load_pickle


STORIES = [
    'announcement_of_the_IBM_704',
    'beginnings_of_cs_at_mit',
    'cost_of_using_a_supercomputer',
    'digital_humanities',
    'network_story',
    'qualifications_for_programmer',
    'three_man_months',
    'women_in_symbols',
    'whirlwind',
]


def index(request):
    story_selection = random.sample(STORIES, 6)
    context = {'stories': story_selection}
    return render(request, 'index.jinja2', context)


def stories(request):
    template = 'archives/stories.jinja2'
    context = {'stories': STORIES}
    return render(request, template, context)


def about(request):
    return render(request, 'archives/about.jinja2')


def create_doc_list(doc_qs):
    """ Helper function for person() and organization() """
    doc_list = []
    for doc in doc_qs:
        doc_list.append({
            'document_date': str(doc.date) if doc.date else 'Unknown',
            'document_title': f'<a href="{doc.url}">{doc.title}</a>',
        })
    return doc_list

# TODO(ra): person and organization should be one view, but they can't be
# compressed right now because the 'related_name' field on Document
# is different. They should share related names, which would simplify this
# view logic.

def person(request, slug):
    person_obj = get_object_or_404(
        Person.objects.prefetch_related(
            'author_person',
            'recipient_person',
            'cced_person',
        ),
        slug=slug)

    docs_written_qs = person_obj.author_person.all()
    docs_written_list = create_doc_list(docs_written_qs)

    docs_received_qs = person_obj.recipient_person.all()
    docs_received_list = create_doc_list(docs_received_qs)

    docs_cced_qs = person_obj.cced_person.all()
    docs_cced_list = create_doc_list(docs_cced_qs)

    obj_dict = {
        'person': person_obj,
        'docs_written_list': docs_written_list,
        'docs_received_list': docs_received_list,
        'docs_cced_list': docs_cced_list,
    }
    return render(request, 'archives/person_or_org.jinja2', obj_dict)


def organization(request, slug):
    org = get_object_or_404(
        Organization.objects.prefetch_related(
            'author_organization',
            'recipient_organization',
            'cced_organization',
        ),
        slug=slug)

    docs_written_qs = org.author_organization.all()
    docs_written_list = create_doc_list(docs_written_qs)

    docs_received_qs = org.recipient_organization.all()
    docs_received_list = create_doc_list(docs_received_qs)

    docs_cced_qs = org.cced_organization.all()
    docs_cced_list = create_doc_list(docs_cced_qs)

    obj_dict = {
        'org': org,
        'docs_written_list': docs_written_list,
        'docs_received_list': docs_received_list,
        'docs_cced_list': docs_cced_list,
    }
    return render(request, 'archives/person_or_org.jinja2', obj_dict)


def get_neighboring_docs(doc_obj):
    """
    :param doc_obj:
    :return: tuple that holds (previous_doc, next_doc) - if doc doesn't exist return False instead
    """

    filename_split = doc_obj.file_name.split("_")

    doc_number = int(filename_split[-1])

    previous_doc_number = doc_number - 1
    next_doc_number = doc_number + 1

    filename_split[-1] = str(previous_doc_number)
    previous_doc_file_name = "_".join(filename_split)

    filename_split[-1] = str(next_doc_number)
    next_doc_file_name = "_".join(filename_split)

    try:
        previous_doc = Document.objects.get(file_name=previous_doc_file_name)
    except ObjectDoesNotExist:
        previous_doc = None

    try:
        next_doc = Document.objects.get(file_name=next_doc_file_name)
    except ObjectDoesNotExist:
        next_doc = None

    return previous_doc, next_doc


def doc(request, slug=None):
    """
    Puts a document on the screen
    :param request:
    :param slug:
    :return:
    """
    if slug:
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
    authors = list(author_person_objs) + list(author_organization_objs)

    recipient_person_objs = doc_obj.recipient_person.all()
    recipient_organization_objs = doc_obj.recipient_organization.all()
    recipients = list(recipient_person_objs) + list(recipient_organization_objs)

    cced_person_objs = doc_obj.cced_person.all()
    cced_organization_objs = doc_obj.cced_organization.all()
    cced = list(cced_person_objs) + list(cced_organization_objs)

    prev_doc, next_doc = get_neighboring_docs(doc_obj)
    
    obj_dict = {
        'doc_obj': doc_obj,
        'authors': authors,
        'recipients': recipients,
        'cced': cced,
        'prev_doc': prev_doc,
        'next_doc': next_doc,
        'no_header': True
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
    folder = get_object_or_404(Folder, slug=slug)
    doc_qs = folder.document_set.all()
    doc_list = []
    for doc in doc_qs:
        doc_list.append({
            'doc_id': doc.doc_id,
            'document_date': str(doc.date) if doc.date else 'Unknown',
            'document_title': f'<a href="{doc.url}">{doc.title}</a>',
        })

    obj_dict = {
        'folder': folder,
        'doc_list': doc_list,
    }
    response = render(request, 'archives/folder.jinja2', obj_dict)

    return response


def list_obj(request, model_str):

    if model_str in ['people', 'organizations', 'folders']:
        obj_list = load_pickle(f'{model_str}_list')
    else:
        raise NotImplementedError(f'List view is not implemented for {model_str} model.')

    obj_dict = {
        'model_str': model_str,
        'obj_list': obj_list
    }

    response = render(request, 'archives/list.jinja2', obj_dict)
    return response


def search(request):
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

    context = {'no_header': True, 'doc_types': doc_types}

    # if no search_params, that means we're just loading the search page
    search_params = request.GET
    if not search_params:
        return render(request, 'archives/search.jinja2', context) 

    search_result = process_search(search_params)
    if search_result:
        docs_result, people_result, search_facets = search_result
    else: # search was run with no params
        return render(request, 'archives/search.jinja2', context)

    search_objs = {
        'docs': docs_result,
        'people': people_result,
        'search_facets': search_facets,
        'search_params': search_params,
    }
    context = {**context, **search_objs}

    return render(request, 'archives/search.jinja2', context)


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

    if 'node' in request.GET:
        old_query = request.GET['node']
        search_node = old_query.lower()
    else:
        search_node = None
        old_query = None

    # if no search is specified, sort out top 100 nodes
    if not search_node:
        # Sorts out everything but the top 100 nodes
        nodes = sorted(nodes, key=lambda i: i['weight'], reverse=True)[:100]
        node_list = [i['id'] for i in nodes]

        # Removes all links that connect to nodes that no longer exist
        links = [i for i in links if i['source'] in node_list and i['target'] in node_list]

    # Otherwise, find applicable nodes and edges
    else:
        # Remove links that don't include the relevant node
        links = [i for i in links if search_node in i['source'].lower() or
                 search_node in i['target'].lower()]
        valid_nodes = []
        for link in links:
            valid_nodes.append(link['source'])
            valid_nodes.append(link['target'])

        # Removes nodes that aren't in the list of links
        nodes = [i for i in nodes if i['id'] in valid_nodes]

    graph_dict = {'nodes': nodes, 'links': links, 'old_query': old_query}
    return render(request, 'archives/net_viz.jinja2', graph_dict)


def timeline(request):
    documents = (Document.objects.order_by('date').exclude(date=None))
    last_year = documents.last().date.year
    documents_by_year = {}
    documents_by_year["1945-1949"] = []
    for i in range(1950, last_year + 1):
        documents_by_year[i] = []
    for document in documents:
        year = document.date.year
        if year < 1950:
            documents_by_year["1945-1949"].append(document)
        else:
            documents_by_year[year].append(document)
    context = {'documents_by_year': documents_by_year}
    return render(request, 'archives/timeline.jinja2', context)


def all_docs(request):
    """ We're not going to show this publically (probably) -- this is for metadata cleaning """
    docs = (Document.objects.all()
                           .order_by('folder__box__number', 'folder__number', 'doc_id')
                           .prefetch_related('folder', 'folder__box'))

    return render(request, 'archives/all_docs.jinja2', {'docs': docs})

