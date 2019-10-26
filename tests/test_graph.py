import pytest
from graph import (
    RandomGraph,
    connected_components,
    mst_prim
)
from utils import (
    np
)
import networkx

#TODO: add some tests

np.random.seed(31415)

# skeleton

def test_cc():
    graph = RandomGraph()
    assert networkx.number_connected_components(graph)

def test_connected_graph():
    graph = RandomGraph()
    assert (networkx.is_connected(graph))

def test_mst_prim():
    pass

if __name__ == "__main__":
    pytest.main()
