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




class Network():

    def __init__(self):

        self.nodes = {}
        self.edges = {}

        df = get_metadata()
        for document_metadata in df.iterrows():

            document_metadata = document_metadata[1]

            document = Document(document_metadata)

            # add the new document to the author node
            print(document.author)
            if document.author not in self.nodes:
                self.nodes[document.author] = Node(document.author)
            self.nodes[document.author].add_document(document)

            if document_metadata['recipients'] not in [None, 'None']:
                self._add_edge(document)

    def _add_edge(self, document):

        author = document.author
        recipient = document.recipients
        for name in [author, recipient]:
            if not name in self.nodes:
                self.nodes[name] = Node(name)
        if not (author, recipient) in self.edges:
            self.edges[(author, recipient)] = Edge(author, recipient)
        self.edges[(author, recipient)].add_document(document)


class Node():

    def __init__(self, name):
        self.name = name
        self.documents = []

    def __repr__(self):
        return f"Node: {self.name}"

    def __eq__(self, other):

        if self.name == other.name:
            return True
        else:
            return False

    def __len__(self):
        return len(self.documents)

    def add_document(self, document):
        self.documents.append(document)


class Edge():

    def __init__(self, author, recipient):
        self.author = author
        self.recipient = recipient
        self.documents = []

    def __repr__(self):
        return f"Edge. Author: {self.author}. Recipient: {self.recipient}"

    def __eq__(self, other):

        if (self.author == other.author and self.recipient == other.recipient) or \
           (self.author == other.recipient and self.recipient == other.author):
            return True
        else:
            return False

    def __len__(self):
        return len(self.documents)

    def add_document(self, document):
        self.documents.append(document)



class Document():

    def __init__(self, document_metadata):
        self.date = document_metadata['date']
        self.doc_type = document_metadata['type']
        self.author = document_metadata['author']
        self.title = document_metadata['title']
        self.filename = document_metadata['filename']

        if document_metadata['recipients'] == 'None':
            self.recipients = None
        else:
            self.recipients = document_metadata['recipients']





if __name__ == '__main__':

    create_network_graph_weighted()

