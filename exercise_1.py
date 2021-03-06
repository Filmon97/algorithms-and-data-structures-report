from utils import (
    np,
    evaluate,
    plot_data,
    plot_compare
)

# the np.random.seed(...) is included
# in the setup variabile
filepath = './images/exercise_1/'
# global range(start,end,offset)
start = 100
end = 20_100
offset = 1000

def worst_case_insertion_sort(n):
    setup = """
from sort import (insertion_sort)
from utils import (np,gen_reversed_array)
np.random.seed(31415)
s = gen_reversed_array({})
gc.enable()
    """.format(n)
    return evaluate(stmt='insertion_sort(s)', setup=setup, repeat=10)


def best_case_insertion_sort(n):
    setup = """
from sort import (insertion_sort)
from utils import (np,gen_sorted_array)
np.random.seed(31415)
s = gen_sorted_array({})
gc.enable()
    """.format(n)
    return evaluate(stmt='insertion_sort(s)', setup=setup, repeat=10)


def avg_case_insertion_sort(n):
    setup = """
from sort import (insertion_sort)
from utils import (np,gen_random_n_array)
np.random.seed(31415)
s = gen_random_n_array({})
gc.enable()
    """.format(n)
    return evaluate(stmt='insertion_sort(s)', setup=setup, repeat=10)

def avg_case_quick_sort(n):
    setup = """
from sort import (quick_sort)
from utils import (np,gen_random_n_array)
np.random.seed(31415)
s = gen_random_n_array({})
gc.enable()
    """.format(n)
    return evaluate(stmt='quick_sort(s,0,len(s)-1)', setup=setup, repeat=10)


def worst_case_quick_sort(n):
    setup = """
from sort import (quick_sort)
from utils import (np,gen_sorted_array)
np.random.seed(31415)
s = gen_sorted_array({})
gc.enable()
    """.format(n)
    return evaluate(stmt='quick_sort(s,0,len(s)-1)', setup=setup, repeat=10)


def experiment_b_c_i_s():
    r = range(start, end, offset)
    times = []
    for i in r:
        times.append(best_case_insertion_sort(i))

    plot_data(r, times, "best case insertion sort", "Sorting", "n", "time")

def experiment_w_c_q_s():
    r = range(start, end, offset)
    times = []
    for i in r:
        times.append(worst_case_quick_sort(i))

    plot_data(r, times, "worst case quick sort", "Sorting", "n", "time")


def experiment_w_c_i_s():
    r = range(start, end, offset)
    times = []
    for i in r:
        times.append(worst_case_insertion_sort(i))

    plot_data(r, times, "worst case insertion sort", "Sorting", "n", "time")


def experiment_a_c_i_s():
    r = range(start, end, offset)
    times = []
    for i in r:
        times.append(avg_case_insertion_sort(i))

    plot_data(r, times, "average case insertion sort", "Sorting", "n", "time")


def experiment_a_c_q_s():
    r = range(start, end, offset)
    times = []
    for i in r:
        times.append(avg_case_quick_sort(i))

    plot_data(r, times, "average case quick sort", "Sorting", "n", "time")


def experiment_b_c_c():
    r = range(start, end, offset)
    times_quick = []
    times_inser = []
    for i in r:
        times_quick.append(avg_case_quick_sort(i))
        times_inser.append(best_case_insertion_sort(i))

    plot_compare(r, times_quick, times_inser, "best(avg) case quick sort",
                 "best case insertion sort", "Sorting", "n", "time", filepath+'bestcase.png')


def experiment_w_c_c():
    r = range(start, end, offset)
    times_quick = []
    times_inser = []
    for i in r:
        times_quick.append(worst_case_quick_sort(i))
        times_inser.append(worst_case_insertion_sort(i))

    plot_compare(r, times_quick, times_inser, "worst case quick sort",
                 "worst case insertion sort", "Sorting", "n", "time", filepath+'worstcase.png')


def experiment_a_c_c():
    r = range(start, end, offset)
    times_quick = []
    times_inser = []
    for i in r:
        times_quick.append(avg_case_quick_sort(i))
        times_inser.append(avg_case_insertion_sort(i))

    plot_compare(r, times_quick, times_inser, "average case quick sort",
                 "average case insertion sort", "Sorting", "n", "time", filepath+'averagecase.png')


if __name__ == "__main__":
    experiment_a_c_c()
    experiment_b_c_c()
    experiment_w_c_c()