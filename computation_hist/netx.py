import matplotlib.pyplot as plt

# from common import get_metadata_google_sheet
from document import Document
import csv
import networkx as nx
import plotly
import plotly.graph_objs as go

# This is a file for testing to see if the class system in networks.py can be updated with a more
# linear setup through networkx


def make_graph(max_nodes=None, debug=False):
    """
    Takes in a metadata sheet from Google Drive and makes a networkx graph of the data, with authors
    as nodes and correspondence as the edges.
    >>> g = make_graph(debug=True)
    >>> len(g.nodes())
    11

    :param debug:
    :return: networkx graph object
    """
    # if (max_nodes is not None) or (not isinstance(max_nodes, int)):
    #     raise ValueError(f'max_nodes must be None or int, not {type(max_nodes)}')

    graph = nx.DiGraph()

    # For debugging purposes
    if debug:
        with open('computation_hist/data/sample_docs/test.csv', 'r') as file:  #
            metadata = csv.DictReader(file)
            for document_metadata in metadata:
                add_doc(graph, document_metadata)

    # The Google Drive metadata
    else:
        metadata = get_metadata_google_sheet(return_type='list_of_dicts')
        add_doc(graph, metadata)

    if max_nodes is None:
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
    if 'None' in recipients:
        recipients.remove('None')

    # Adds author to the graph or increases the weight of the node
    if author not in graph:
        graph.add_node(author, weight=1)
    else:
        graph.nodes[author]['weight'] += 1

    # Adds edges based on who the letter has been sent to
    if recipients:
        for recip in recipients:
            if recip not in graph:
                graph.add_node(recip, weight=1)

            if (author, recip) not in graph.edges:
                graph.add_edge(author, recip, weight=1)

            else:
                graph.edges[author, recip]['weight'] += 1

    # If the list of recipients is empty, use 'None' as the recipient
    else:
        if 'None' not in graph:
            graph.add_node('None', weight=1)

        if (author, 'None') not in graph.edges:
            graph.add_edge(author, 'None', weight=1)
        else:
            graph.edges[author, 'None']['weight'] += 1


def basic_draw(graph):
    """
    This provides a very simple network graph through matplotlib, ideal for speed but not
    necessarily very pretty

    :param graph: networkx Graph object
    :return: None
    """
    nx.draw_circular(graph,
                     with_labels=True,
                     node_size=[node[1] * 100 for node in g.nodes.data('weight')],
                     width=[edge[2] for edge in g.edges.data('weight')]
                     )
    plt.show()


if __name__ == '__main__':
    g = make_graph(debug=True)
    basic_draw(g)


