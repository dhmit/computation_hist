import matplotlib.pyplot as plt

# from common import get_metadata_google_sheet
from document import Document
import csv


class Network:
    """
    The network class currently provides a skeleton to do social network analysis. It is meant
    to be expanded and all of the current functions can be modified or deleted.

    It currently creates a directed network (i.e. the same node pair can have two edges, one where
    they are

    >>> network = Network()
    >>> network
    Network with 43 nodes and 56 edges

    # The network has a dict of nodes that map from a person to a Node object
    >>> node = network.nodes['Morse, Philip M.']
    >>> print(f'{node}. Number of documents authored by node: {len(node)}')
    Node: Morse, Philip M.. Number of documents authored by node: 4

    # Similarly, it has a dict of edges that map from an (author, recipient) tuple to an Edge object
    >>> edge = list(network.edges.values())[0]
    >>> print(f'{edge}. Number documents for this edge: {len(edge)}')
    Edge. Author: Corbato, F. J.. Recipient: Verzuh, F. M.. Number documents for this edge: 1

    # The main purpose for this class for the time being is to visualize the network arising from
    # the metadata (for some reason, this doctest passes)
    >>> network.visualize_network(no_nodes=20)
    """

    def __init__(self, return_empty_network=False, debug=False):

        # nodes and edges are dicts that map from node_name to a Node object
        # and from (edge_author, edge_recipient) to an Edge object.
        # there's probably a better way of storing this data
        self.nodes = {}
        self.edges = {}

        # initialize network using the available metadata
        if not return_empty_network:

            # For debugging purposes
            if debug:
                with open('computation_hist/data/sample_docs/verzuh_metadata.csv', 'r') as file:  #
                    metadata = csv.DictReader(file)
                    for document_metadata in metadata:
                        self._add_document_to_network(document_metadata)
            else:
                metadata = get_metadata_google_sheet(return_type='list_of_dicts')
                self._add_document_to_network(metadata)

    def __repr__(self):
        return f'Network with {len(self.nodes)} nodes and {len(self.edges)} edges'

    def _add_document_to_network(self, document_metadata):
        """
        Adds one document to the network

        >>> network = Network(return_empty_network=True)
        >>> metadata = {'box': 2, 'foldername_short': 'verzuh', 'doc_id': 1,
        ...            'filename': '2_verzuh_1', 'author': 'Corbato, F. J.', 'title': 'n/a',
        ...             'date': '1957-11-21', 'text': 'Sample text...', 'recipients': 'Morse'}
        >>> network._add_document_to_network(metadata)
        >>> network
        Network with 2 nodes and 1 edges

        """

        document_metadata['text'] = ''
        document = Document(document_metadata)

        # add the new document to the author node
        if document.author not in self.nodes:
            self.nodes[document.author] = Node(document.author)
        self.nodes[document.author].add_document(document)

        # if the document has recipients, add them as nodes if necessary and add all of the edges
        if document.recipients:
            author = document.author
            recipients = document.recipients
            for name in recipients:
                if name not in self.nodes:
                    self.nodes[name] = Node(name)
            for recipient in recipients:
                if (author, recipient) not in self.edges:
                    author_node = self.nodes[author]
                    recipient_node = self.nodes[recipient]
                    self.edges[(author, recipient)] = Edge(author_node, recipient_node)
                self.edges[(author, recipient)].add_document(document)

    def visualize_network(self, no_nodes=20):
        """
        Visualizes the network as a circular graph that includes up to no_nodes nodes.
        TODO: Add more configuration options (different layouts, colors, node and edge selections)

        # use the no_nodes param to define how many nodes to show
        >>> network = Network()
        >>> network.visualize_network(no_nodes=20)

        """

        import networkx as nx
        graph = nx.Graph()
        # include top no_nodes that authored most documents.
        included_nodes = [node for node in sorted(self.nodes.values(),
                                                  key=lambda x: len(x), reverse=True)][:no_nodes]
        for node in included_nodes:
            graph.add_node(node.name, weight=len(node))
        for edge in self.edges.values():
            if edge.author in included_nodes and edge.recipient in included_nodes:
                graph.add_edge(edge.author.name, edge.recipient.name, weight=len(edge))
        labels = {node.name: node.name for node in included_nodes}

        nx.draw_circular(graph,
                         labels=labels,
                         node_size=[len(node) * 100 for node in self.nodes.values()],
                         width=[len(edge) for edge in self.edges.values()]
                         )
        plt.show()


class Node:
    """
    Class to store nodes for the Network class. Each node consists of a name and a list of documents

    """

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


class Edge:
    """
    Class to store edges for the Network class.
    Each Edge consists of an author Node, a recipient Node, and a list of documents exchanged
    between them.

    """

    def __init__(self, author: Node, recipient: Node):
        self.author = author
        self.recipient = recipient
        self.documents = []

    def __repr__(self):
        return f"Edge. Author: {self.author.name}. Recipient: {self.recipient.name}"

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


if __name__ == '__main__':
    n = Network(debug=True)
    for i in n.nodes:
        print(n.nodes[i], len(n.nodes[i]))

    for i in n.edges:
        print(n.edges[i], len(n.edges[i]))

    print('Number of Nodes:', len(n.nodes))
    n.visualize_network()