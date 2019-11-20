from utils import (
    np,
    evaluate,
    plot_data
)
from graph import (RandomGraph)

start = 100
end = 2100
offset = 100


def connected_components(n):
    setup = """
from graph import (SavedGraph, connected_components)
from utils import (np)
np.random.seed(31415)
filename = './graphs/graph'
graph = SavedGraph(filename+str({}))
gc.enable()
    """.format(n)

    return evaluate(stmt='connected_components(graph)', setup=setup, repeat=10)

#for testing
#_________________________________________________________________________________________________
def build_graph():
    filename = './graphs/graph'
    for i in range(start,end,offset):
        RandomGraph(list(range(i))).save_graph(filename+str(i))

def create_graph(n):
    setup = """
from graph import (RandomGraph)
from utils import (np)
np.random.seed(31415)
gc.enable()
    """
    return evaluate(stmt='graph = RandomGraph(list(range({})))'.format(n), setup=setup, repeat=10)

def load_graph(n):
    setup = """
from graph import (SavedGraph)
from utils import (np)
np.random.seed(31415)
filename = './graphs/graph'
gc.enable()
    """
    return evaluate(stmt='graph = SavedGraph(filename+str({}))'.format(n), setup=setup, repeat=10)
#_________________________________________________________________________________________________


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
    r = range(start, end, offset)
    times = []
    for i in r:
        times.append(uniform_graph_mst_prim(i))

    plot_data(r, times, "Prim", "Minimum Spanning Tree", "n", "time")

def experiment_cc():
    r = range(start, end, offset)
    times = []
    for i in r:
        times.append(connected_components(i))

    plot_data(r, times, "Connected Components", "Minimum Spanning Tree", "n", "time")


if __name__ == "__main__":
    #experiment_mst_prim()
    experiment_cc()