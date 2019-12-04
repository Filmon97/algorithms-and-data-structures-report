from utils import (
    evaluate,
    plot_data,
    plot_compare
)

# the np.random.seed(...) is included
# in the setup variabile
start = 100
end = 2100
offset = 100

filepath = './images/exercise_A/'


def insertion_bst(n):
    setup = """
from tree import (BinarySearchTree)
from utils import (np,gen_random_u_array)
np.random.seed(31415)
data = gen_random_u_array({})
bst = BinarySearchTree()
gc.enable()
    """.format(n)
    return evaluate(stmt='for d in data: bst.insert(d)', setup=setup, repeat=10)


def insertion_rbt(n):
    setup = """
from tree import (RedBlackTree)
from utils import (np,gen_random_u_array)
np.random.seed(31415)
data = gen_random_u_array({})
rbt = RedBlackTree()
gc.enable()
    """.format(n)
    return evaluate(stmt='for d in data: rbt.insert(d)', setup=setup, repeat=10)


def search_bst(n):
    setup = """
from tree import (BinarySearchTree)
from utils import (np,gen_random_u_array)
np.random.seed(31415)
data = gen_random_u_array({})
bst = BinarySearchTree()
for d in data:
    bst.insert(d)
gc.enable()
    """.format(n)
    return evaluate(stmt='bst.find(np.random.choice(data))', setup=setup, repeat=10)


def search_rbt(n):
    setup = """
from tree import (RedBlackTree)
from utils import (np,gen_random_u_array)
np.random.seed(31415)
data = gen_random_u_array({})
rbt = RedBlackTree()
for d in data:
    rbt.insert(d)
gc.enable()
    """.format(n)
    return evaluate(stmt='rbt.find(np.random.choice(data))', setup=setup, repeat=10)


def experiment_i_bst():
    r = range(start, end, offset)
    times = []
    for i in r:
        times.append(insertion_bst(i))

    plot_data(r, times, "BinarySearchTree", "Insertion", "n", "time")


def experiment_i_rbt():
    r = range(start, end, offset)
    times = []
    for i in r:
        times.append(insertion_rbt(i))

    plot_data(r, times, "RedBlackTree", "Insertion", "n", "time")


def experiment_s_bst():
    r = range(start, end, offset)
    times = []
    for i in r:
        times.append(search_bst(i))

    plot_data(r, times, "BinarySearchTree", "Search", "n", "time")


def experiment_s_rbt():
    r = range(start, end, offset)
    times = []
    for i in r:
        times.append(search_rbt(i))

    plot_data(r, times, "RedBlackTree", "Search", "n", "time")


def experiment_i_compare():
    r = range(start, end, offset)
    times_bst = []
    times_rbt = []
    for i in r:
        times_bst.append(insertion_bst(i))
        times_rbt.append(insertion_rbt(i))

    plot_compare(r, times_bst, times_rbt, "BinarySearchTree",
                 "RedBlackTree", "Insertion", "n", "time", filepath+'insertion.png')


def experiment_s_compare():
    r = range(start, end, offset)
    times_bst = []
    times_rbt = []
    for i in r:
        times_bst.append(search_bst(i))
        times_rbt.append(search_rbt(i))

    plot_compare(r, times_bst, times_rbt, "BinarySearchTree",
                 "RedBlackTree", "Search", "n", "time", filepath+'search.png')


if __name__ == "__main__":
    experiment_i_compare()
    experiment_s_compare()
