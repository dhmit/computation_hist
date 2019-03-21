import matplotlib.pyplot as plt
import operator
import math

# from common import get_metadata_google_sheet
from document import Document
import csv
import networkx as nx
import plotly
import plotly.graph_objs as go
from pathlib import Path


def make_graph(max_nodes=None, debug=False):
    """
    Takes in a metadata sheet from Google Drive and makes a networkx graph of the data, with authors
    as nodes and correspondence as the edges. Declaring max_nodes as an int n will return a Graph
    object with only the n-th largest nodes.

    >>> g = make_graph(debug=True, max_nodes=50)
    >>> list(g.nodes)[2:5]
    ['Corbato, F. J.', 'None', 'unknown']



    :param max_nodes: int or None
    :param debug: Boolean
    :return: networkx graph object
    """
    if isinstance(max_nodes, type(int)):
        raise ValueError(f'max_nodes must be None or int, not {type(max_nodes)}')

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
    else:
        removed_nodes = list(graph.nodes(data='weight'))
        removed_nodes.sort(key=operator.itemgetter(1))
        removed_nodes = removed_nodes[:-max_nodes]
        names = [node[0] for node in removed_nodes]
        graph.remove_nodes_from(names)
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
    if author is '':
        author = 'None'
    if 'None' in recipients:
        recipients.remove('None')
    if '' in recipients:
        recipients.remove('')

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

            graph.nodes[author]['weight'] += 1

            if (author, recip) not in graph.edges:
                graph.add_edge(author, recip, weight=1)

            else:
                graph.edges[author, recip]['weight'] += 1

    # If the list of recipients is empty, use 'None' as the recipient
    else:
        if 'None' not in graph:
            graph.add_node('None', weight=1)

        graph.nodes['None']['weight'] += 1

        if (author, 'None') not in graph.edges:
            graph.add_edge(author, 'None', weight=1)
        else:
            graph.edges[author, 'None']['weight'] += 1


def basic_draw(graph, directed=True):
    """
    This provides a very simple network graph through matplotlib, ideal for speed but not
    necessarily very pretty.

    :param graph: networkx Graph object
    :param directed: Boolean
    :return: None
    """

    if directed:
        g = graph
    else:
        g = nx.Graph(graph)

    nx.draw_circular(g,
                     with_labels=True,
                     font_size=10,
                     font_color='b',
                     font_shadow='w',
                     node_size=[node[1] * 10 for node in g.nodes.data('weight')],
                     width=[max(edge[2] // 4, 1) for edge in g.edges.data('weight')]
                     )
    plt.show()


def fancy_network(g):
    """
    Draws a prettier network graph using Plotly. Note that this does not support directed graphs
    and displays a constant edge width.

    :param g: Networkx Graph object
    :return: None
    """

    # Set up the nodes in a circle
    angle_inc = 2*math.pi/len(g.nodes)
    theta = 0
    for node in g.nodes:
        x = math.cos(theta)
        y = math.sin(theta)
        g.nodes[node]['pos'] = (x, y)
        theta += angle_inc

    edge_trace = go.Scatter(
        x=[],
        y=[],
        line=dict(width=1, color='#888'),
        hoverinfo='none',
        mode='lines'
        )

    for edge in g.edges():
        x0, y0 = g.node[edge[0]]['pos']
        x1, y1 = g.node[edge[1]]['pos']
        edge_trace['x'] += tuple([x0, x1, None])
        edge_trace['y'] += tuple([y0, y1, None])

    node_trace = go.Scatter(
        x=[],
        y=[],
        text=[],
        mode='markers',
        hoverinfo='text',
        marker=dict(
            showscale=True,
            colorscale='Bluered',
            reversescale=True,
            color=[],
            size=[],
            colorbar=dict(
                thickness=15,
                title='Letters Sent/Received',
                xanchor='left',
                titleside='right'
            ),
            line=dict(width=2)))

    for node in g.nodes():
        x, y = g.node[node]['pos']
        node_trace['x'] += tuple([x])
        node_trace['y'] += tuple([y])

    # colors nodes based on weight
    for node in g.nodes:
        node_trace['marker']['color'] += tuple([g.nodes[node]['weight']])
        node_trace['marker']['size'] += tuple([max(g.nodes[node]['weight'] // 4, 30)])
        node_info = node + '<br># of letters: ' + str(g.nodes[node]['weight'])
        node_trace['text'] += tuple([node_info])

    fig = go.Figure(data=[edge_trace, node_trace],
                    layout=go.Layout(
                        title='<br>Network Graph from Metadata',
                        titlefont=dict(size=16),
                        showlegend=False,
                        hovermode='closest',
                        margin=dict(b=20, l=5, r=5, t=40),
                        annotations=[dict(
                            showarrow=True,
                            xref="paper", yref="paper",
                            x=0.005, y=-0.002)],
                        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False)))

    plotly.offline.plot(fig, filename='computation_hist/data/network.html')


def graph_to_csv(graph,
                 node_path='computation_hist/data/nodes.csv',
                 edge_path='computation_hist/data/edges.csv'):
    """

    :param graph: Networkx Graph object
    :param node_path: Path or str object
    :param edge_path: Path or str object
    :return: None
    """
    if isinstance(node_path, str):
        node_path = Path(node_path)
    if not isinstance(node_path, Path):
        raise ValueError('node_path must be a str or Path object, not ' + str(type(node_path)))
    if isinstance(edge_path, str):
        edge_path = Path(edge_path)
    if not isinstance(edge_path, Path):
        raise ValueError('node_path must be a str or Path object, not ' + str(type(edge_path)))

    edges = graph.edges.keys()
    nodes = graph.nodes.keys()

    # Set up Nodes
    with open(node_path, 'w') as file:
        headers = ['node', 'weight']
        writer = csv.writer(file)

        writer.writerow(headers)
        for node in nodes:
            writer.writerow([node, graph.nodes[node]['weight']])

    # Set up Edges
    with open(edge_path, 'w') as file:
        headers = ['author', 'recipient', 'weight']
        writer = csv.writer(file)

        writer.writerow(headers)
        for edge in edges:
            writer.writerow([edge[0], edge[1], graph.edges[edge]['weight']])


if __name__ == '__main__':
    graph = make_graph(debug=True, max_nodes=10)
    graph_to_csv(graph)
