
# TODO:
# add comparing cases
# for op. on BST and RNT


# TODO:
# add the experiments

from utils import *

## the np.random.seed(...) is included
## in the setup variabile

def insertion_bst(n):
    setup = """
from tree import (BinarySearchTree)
from utils import (np,gen_random_u_array)
np.random.seed(31415)
data = gen_random_u_array({})
bst = BinarySearchTree()
gc.enable()
    """.format(n)
    return min(timeit.Timer('for d in data: bst.insert(d)', setup=setup).repeat(10, 1))

def insertion_rn(n):
    setup = """
from tree import (RedBlackTree)
from utils import (np,gen_random_u_array)
np.random.seed(31415)
data = gen_random_u_array({})
rn = RedBlackTree()
gc.enable()
    """.format(n)
    return min(timeit.Timer('for d in data: rn.insert(d)', setup=setup).repeat(10, 1))

def experiment_i_bst():
    r = range(100, 2100, 100)
    times = []
    for i in r:
        times.append(insertion_bst(i))

    plot_data(r, times, "BinarySearchTree", "Insertion", "n", "time")

def experiment_i_rn():
    r = range(100, 2100, 100)
    times = []
    for i in r:
        times.append(insertion_rn(i))

    plot_data(r, times, "RedBlackTree", "Insertion", "n", "time")


if __name__ == "__main__":
    experiment_i_bst()
    experiment_i_rn()