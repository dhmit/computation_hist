import random
import re
from collections import Counter

from django.db.models import Q
from django.http import Http404
from django.shortcuts import get_list_or_404, get_object_or_404, render
from django.template.loader import TemplateDoesNotExist
from django.core.exceptions import ObjectDoesNotExist

from utilities.common import get_file_path
from .models import Person, Document, Box, Folder, Organization
from .search import process_search


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
    'whirlwind',
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

    prev_doc, next_doc = get_neighboring_docs(doc_obj)

    obj_dict = {
        'doc_obj': doc_obj,
        'author_person_objs': author_person_objs,
        'author_organization_objs': author_organization_objs,
        'recipient_person_objs': recipient_person_objs,
        'recipient_organization_objs': recipient_organization_objs,
        'cced_person_objs': cced_person_objs,
        'cced_organization_objs': cced_organization_objs,
        'doc_pdf_url': doc_pdf_url,
        'prev_doc': prev_doc,
        'next_doc': next_doc,
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


def person_unknown_filter(person):
    if person.last == "":
        person.last = "Unknown"
    return person.last


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
        model_objs.sort(key=person_unknown_filter)
    elif model_str == "folder":
        model_objs = get_list_or_404(Folder.objects.prefetch_related('box'))
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


def browse(request):
    return render(request, 'archives/browse.jinja2')


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

    # if no search_params, that means we're just loading the search page
    search_params = request.GET
    if not search_params:
        return render(request, 'archives/search.jinja2', {'doc_types': doc_types})

    search_result = process_search(search_params)
    if search_result:
        docs_result, people_result, search_facets = search_result
    else: # search was run with no params
        return render(request, 'archives/search.jinja2', {'doc_types': doc_types})

    search_objs = {
        'docs': docs_result,
        'people': people_result,
        'search_facets': search_facets,
        'search_params': search_params,
        'doc_types': doc_types
    }
    return render(request, 'archives/search.jinja2', search_objs)


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
    print(request.GET)

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


def stories(request):
    template = 'archives/stories.jinja2'
    context = {'stories': STORIES}
    return render(request, template, context)

