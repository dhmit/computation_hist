from apps.archives.models import Document
from collections import Counter


def create_network_json():
    """
    # get all documents
    all_docs = Document.objects.all()

    one_doc= all_docs[0]

    authors_one_doc = one_doc.author_person.all()
    edge_counter = Counter()

    first_author_name = authors_one_doc[0].fullname
    for doc in documents:
        for author in authors:
            for recipient in recipients:
                edge_counter[(author.fullname, recipient.fullname)] += 1
    """

    docs = Document.objects.all()
    nodes = Counter()
    edges = Counter()

    for doc in docs:
        for author in doc.author_person.all():
            nodes[author] += 1
            for recip in doc.recipient_person.all():
                edges[(author, recip)] += 1
                nodes[recip] += 1
