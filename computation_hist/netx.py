import matplotlib.pyplot as plt

# from common import get_metadata_google_sheet
from document import Document
import csv
import networkx as nx

# This is a file for testing to see if the class system in networks.py can be updated with a more
# linear setup through networkx


def make_graph(debug=False):
    """
    Takes in a metadata sheet from Google Drive and makes a networkx graph of the data, with authors
    as nodes and correspondence as the edges.
    >>> g = make_graph(debug=True)
    >>> len(g.nodes())
    11

    :param debug:
    :return: networkx graph object
    """

    graph = nx.DiGraph()

    # For debugging purposes
    if debug:
        with open('computation_hist/data/sample_docs/verzuh_metadata.csv', 'r') as file:  #
            metadata = csv.DictReader(file)
            for document_metadata in metadata:
                add_doc(graph, document_metadata)

    # The Google Drive metadata
    else:
        metadata = get_metadata_google_sheet(return_type='list_of_dicts')
        add_doc(graph, metadata)

    return graph


def add_doc(graph, doc_meta):
    """
    Adds a document to a network

    :param graph: a networkx graph object
    :param doc_meta: a dictionary describing a document
    :return:
    """

    doc_meta['text'] = ''
    doc = Document(doc_meta)
    author = doc.author
    recipients = doc.recipients

    # Adds author to the graph or increases the weight of the node
    if author not in graph:
        graph.add_node(author, weight=1)
    else:
        old_weight = graph.nodes(data='weight')[author]
        graph.remove_node(author)
        graph.add_node(author, weight=old_weight + 1)

    # Adds edges based on who the letter has been sent to
    for recip in recipients:
        if recip not in graph:
            graph.add_node(recip)
        else:
            graph.add_edge(author, recip)


if __name__ == '__main__':
    graph = make_graph(debug=True)
    nx.draw(graph, with_labels=True)
    plt.show()

