from collections import Counter

import matplotlib.pyplot as plt
import networkx as nx

from computation_hist.common import get_metadata_google_sheet


# Work with 1_ProjectProposalContract Materials_1
# https://s3-us-west-2.amazonaws.com/computation-hist/scans/project_proposal_contract.pdf


def create_network_graph():

    metadata = get_metadata_google_sheet(return_type='list_of_dicts')

    nodes = set()
    edges = set()

    for document_metadata in metadata:

        author = document_metadata['author']
        recipients = document_metadata['recipients']
        nodes.add(author)
        if recipients not in [None, 'None']:
            nodes.add(recipients)
            edges.add((author, recipients))

    G = nx.Graph()
    for node in nodes:
        G.add_node(node)
    for edge in edges:
        G.add_edge(edge[0], edge[1])

    print(nx.info(G))

    nx.draw_circular(G)
    plt.show()

def create_network_graph_weighted():

    metadata = get_metadata_google_sheet('list_of_dicts')

    nodes = Counter()
    edges = Counter()

    for document_metadata in metadata:
        author = document_metadata['author']
        recipients = document_metadata['recipients']
        nodes[author] += 1
        if recipients not in [None, 'None']:
            nodes[recipients] += 1
            edges[(author, recipients)] += 1

    G = nx.Graph()
    for node in nodes:
        weight = nodes[node]
        G.add_node(node, weight=weight)
    for edge in edges:
        weight = edges[edge]
        G.add_edge(edge[0], edge[1], weight=weight)

    labels = {node: node for node in nodes}

    print(nx.info(G))
    print(nodes.values())

    nx.draw_circular(G,
                     labels=labels,
                     node_size=[i * 100 for i in nodes.values()],
                     width=[i for i in edges.values()]
    )

    plt.show()


if __name__ == '__main__':

    create_network_graph_weighted()

