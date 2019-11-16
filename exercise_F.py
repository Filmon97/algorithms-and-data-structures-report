from utils import (
    np,
    evaluate,
    plot_data
)

def experiment_cc():
    pass

def uniform_graph_mst_prim(n):
    setup = """
from graph import (SavedGraph, mst_prim)
from utils import (np)
filename = './graphs/graph'
np.random.seed(31415)
graph = SavedGraph(filename+str({}))
gc.enable()
    """.format(n)

    return evaluate(stmt='mst_prim(graph,graph.nodes()[0])', setup=setup, repeat=10)


def experiment_mst_prim():
    r = range(100, 2100, 100)
    times = []
    for i in r:
        times.append(uniform_graph_mst_prim(i))

    plot_data(r, times, "Prim", "Minimum Spanning Tree", "n", "time")


if __name__ == "__main__":
    experiment_mst_prim()
