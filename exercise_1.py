from utils import *


### add a limit to timeit repeat
## the np.random.seed(...) is included
## in the setup variabile

def worst_case_insertion_sort(n):
    setup = """
from sort import (insertion_sort)
from utils import (np,gen_reversed_array)
np.random.seed(31415)
s = gen_reversed_array({})
gc.enable()
    """.format(n)
    return min(timeit.Timer('insertion_sort(s)', setup=setup).repeat(10, 1))

def worst_case_quick_sort(n):
    setup = """
from sort import (quick_sort)
from utils import (np,gen_sorted_array)
np.random.seed(31415)
s = gen_sorted_array({})
gc.enable()
    """.format(n)
    return min(timeit.Timer('quick_sort(s,0,len(s)-1)', setup=setup).repeat(10, 1))

def best_case_insertion_sort(n):
    setup = """
from sort import (insertion_sort)
from utils import (np,gen_sorted_array)
np.random.seed(31415)
s = gen_sorted_array({})
gc.enable()
    """.format(n)
    return min(timeit.Timer('insertion_sort(s)', setup=setup).repeat(10, 1))

# FIXME: bad input array
# The best case for Quicksort
#  using last element as pivot
#  is the post-order traversal 
# of the balanced binary search tree.
def best_case_quick_sort(n):
    setup = """
from sort import (quick_sort)
from utils import (np,gen_reversed_array)
np.random.seed(31415)
s = gen_reversed_array({})
gc.enable()
    """.format(n)
    return min(timeit.Timer('quick_sort(s,0,len(s)-1)', setup=setup).repeat(10, 1))

def experiment_b_c_i_s():
    r = range(100, 2100, 100)
    times = []
    for i in r:
        times.append(best_case_insertion_sort(i))

    plot_data(r, times, "best case insertion sort", "Sorting", "n", "time")

def experiment_b_c_q_s():
    r = range(100, 2100, 100)
    times = []
    for i in r:
        times.append(best_case_quick_sort(i))

    plot_data(r, times, "best case quick sort", "Sorting", "n", "time")

def experiment_w_c_q_s():
    r = range(100, 2100, 100)
    times = []
    for i in r:
        times.append(worst_case_quick_sort(i))

    plot_data(r, times, "worst case quick sort", "Sorting", "n", "time")

def experiment_w_c_i_s():
    r = range(100, 2100, 100)
    times = []
    for i in r:
        times.append(worst_case_insertion_sort(i))

    plot_data(r, times, "worst case insertion sort", "Sorting", "n", "time")


if __name__ == "__main__":
    experiment_b_c_i_s()
    experiment_b_c_q_s()
    experiment_w_c_i_s()
    experiment_w_c_q_s()
