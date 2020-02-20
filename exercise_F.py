from utils import (
    np,
    evaluate,
    plot_data,
    os
)
from graph import (RandomGraph)

start = 100
end = 1500
offset = 100

filepath = './images/exercise_F/'


def connected_components(n, filename, p):
    setup = """
from graph import (SavedGraph, connected_components)
from utils import (np)
np.random.seed(31415)
filename = '{}'
graph = SavedGraph(filename+str({}))
gc.enable()
    """.format(filename + '_{}_'.format(p), n)

    return evaluate(stmt='connected_components(graph)', setup=setup, repeat=10)

# for testing
# _________________________________________________________________________________________________


def format_p(p):
    format_p = '_1_'
    if p < 1:
        format_p = '_0_{}_'.format(int(p*10))
    return format_p


def build_graph(filename, p):
    for i in range(start, end, offset):
        RandomGraph(list(range(i)), p).save_graph(
            filename+format_p(p)+str(i))


def create_graph(n):
    setup = """
from graph import (RandomGraph)
from utils import (np)
np.random.seed(31415)
gc.enable()
    """
    return evaluate(stmt='graph = RandomGraph(list(range({})))'.format(n), setup=setup, repeat=10)


def load_graph(n, filename):
    setup = """
from graph import (SavedGraph)
from utils import (np)
np.random.seed(31415)
filename = '{}'
gc.enable()
    """.format(filename)
    return evaluate(stmt='graph = SavedGraph(filename+str({}))'.format(n), setup=setup, repeat=10)
# _________________________________________________________________________________________________


def uniform_graph_mst_prim(n, filename, p):
    setup = """
from graph import (SavedGraph, mst_prim)
from utils import (np)
filename = '{}'
np.random.seed(31415)
graph = SavedGraph(filename+str({}))
gc.enable()
    """.format(filename+format_p(p), n)

    return evaluate(stmt='mst_prim(graph,graph.nodes()[0])', setup=setup, repeat=10)


def experiment_mst_prim(filename, p):
    r = range(start, end, offset)
    times = []
    for i in r:
        times.append(uniform_graph_mst_prim(i, filename, p))

    plot_data(r, times, "Prim", "Minimum Spanning Tree P={}".format(p),
              "n", "time", filepath+format_p(p)+'mstprim.png')


def experiment_cc(filename, p):
    r = range(start, end, offset)
    times = []
    for i in r:
        times.append(connected_components(i, filename, p))

    plot_data(r, times, "Connected Components P={}".format(p), "Minimum Spanning Tree",
              "n", "time", filepath+format_p(p)+'conncomponents.png')


if __name__ == "__main__":
    filepath = './graphs/'
    filename = './graphs/graph'
    if os.path.exists(filepath) is False:
        for p in [0.1, 0.5, 1]:
            build_graph(filename, p)

    for p in [0.1, 0.5, 1]:
        experiment_mst_prim(filename, p)
        experiment_cc(filename, p)
