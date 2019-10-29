import pytest
from graph import (
    RandomGraph,
    ConnectedGraph,
    connected_components,
    mst_prim
)
from utils import (
    np
)
import networkx

# TODO: add some tests

np.random.seed(31415)

# skeleton


def test_cc():
    graph = RandomGraph()
    number_cc = len(connected_components(graph))
    graph_data = networkx.Graph(graph.graph_dict)
    assert networkx.number_connected_components(graph_data) == number_cc


def test_connected_components():
    graph = RandomGraph()
    number_cc = len(connected_components(graph))
    graph_data = networkx.Graph(graph.graph_dict)
    test = networkx.is_connected(graph_data)
    test = number_cc == 1 if test else number_cc != 1
    assert test

def test_connected_graph():
    graph = ConnectedGraph()
    number_cc = len(connected_components(graph))
    assert number_cc == 1

def test_mst_prim():
    graph = RandomGraph()
    mst = mst_prim(graph, graph.nodes()[0])

    nx_graph = networkx.Graph()
    for node in graph.nodes():
        for neighbor in graph.get(node):
            if nx_graph.has_edge(node,neighbor) is False and nx_graph.has_edge(neighbor,node) is False:
                nx_graph.add_edge(node, neighbor, weight=graph.get(node, neighbor))

    tree = []
    for node in mst:
        if mst[node] is not None:
            tree.append((node,mst[node]))
    print(tree)
    
    T = networkx.minimum_spanning_tree(nx_graph)  
    edges = T.edges(data=False)

    # Begin the test
    test = True
    
    # I need to check if (x,y) or (y,x) is in networkx generated mst
    for node in tree:
        x, y = node
        print(x,y)
        test = test and ((x,y) in edges or (y,x) in edges)

    assert test


if __name__ == "__main__":
    pytest.main()
