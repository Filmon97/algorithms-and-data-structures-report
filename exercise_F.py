from graph import (
    RandomGraph,
    mst_prim,
    connected_components
)
from utils import (
    np
)
# TODO:
# add connected components experiment

def experiment_cc():
    graph = RandomGraph()

    return connected_components(graph)

# TODO:
# add experiments with timeit

def experiment_mst_prim():
    graph = RandomGraph()
    mst = mst_prim(graph, graph.nodes()[0])
    tree = []
    for node in mst:
        if mst[node] is not None:
            tree.append((node,mst[node]))
    return tree

if __name__ == "__main__":
    np.random.seed(31415)
    #tree = experiment_mst_prim()
    sets = experiment_cc()
    
    print(sets)