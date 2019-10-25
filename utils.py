"""
Provides some utilities like:
- array generation,
- time and space evaluation
- data structure such as PriorityQueue
- etc
"""

from sortedcontainers import SortedList
import numpy as np
import heapq
import collections
# from statistics import mean
import math
import matplotlib.pyplot as plt
import timeit

# from memory_profiler import profile

infinity = float('inf')

# Set one time the maximum recursion limit
import sys
recursion_limit = 100_000
sys.setrecursionlimit(recursion_limit)

# ______________________________________________________________________________
# Array Generation 


def gen_random_n_array(n=100):
    """ Generate a random array (normal distribution)"""
    return list(np.random.randn(n))


def gen_random_u_array(n=100):
    """ Generate a random array (uniform distribution)"""
    return list(np.random.rand(n))


def gen_sorted_array(n=100):
    """ Generate a sorted random array"""
    return list(SortedList(gen_random_u_array(n)))


def gen_reversed_array(n=100):
    """ Generate a descending sorted random array"""
    return list(reversed(SortedList(gen_random_u_array(n))))


# ______________________________________________________________________________
# Performance Evaluation
    
def evaluate(stmt, setup, repeat):
    return min(timeit.Timer(stmt=stmt, setup=setup).repeat(repeat,1))
    
def plot_data(x, y, label, title, xlabel, ylabel, save=None):
    """ Plot the experiments, support save functionality """
    plt.style.use('seaborn')
    plt.plot(x, y, label=label)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.legend()
    if save:
        plt.savefig(save)
    else:
        plt.show()

#???
#TODO
def plot_compare(x, y, z, label, title, xlabel, ylabel, save=None):
    """ Plot the experiments, support save functionality """
    plt.style.use('seaborn')
    plt.plot(x, y, label=label)
    plt.plot(x, z)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.legend()
    if save:
        plt.savefig(save)
    else:
        plt.show()


# Memory Usage

# Decorator
# append below a function
# the @profile decorator
# import the profiler or 
# run in the console 
## python -m memory_profiler example.py
# Time-based memory usage
# mprof run <executable>
# mprof plot
        
# ______________________________________________________________________________
# Math function

identity = lambda x: x

argmin = min
argmax = max

def distance(a, b):
    """The distance between two (x, y) points."""
    xA, yA = a
    xB, yB = b
    return math.hypot((xA - xB), (yA - yB))

# ______________________________________________________________________________
# Set utils
def make_set(x):
    pass

def union(x, y):
    pass

def find_set(x):
    pass

# ______________________________________________________________________________
# Queues: PriorityQueue


class PriorityQueue:
    """A Queue in which the minimum (or maximum) element (as determined by f and
        order) is returned first.
        If order is 'min', the item with minimum f(x) is
        returned first; if order is 'max', then it is the item with maximum f(x).
        Also supports dict-like lookup."""

    def __init__(self, order='min', f=identity):
        self.heap = []

        if order == 'min':
            self.f = f
        elif order == 'max':  # now item with max f(x)
            self.f = lambda x: -f(x)  # will be popped first
        else:
            raise ValueError("order must be either 'min' or 'max'.")

    def append(self, item):
        """Insert item at its correct position."""
        heapq.heappush(self.heap, (self.f(item), item))

    def insert(self, item, value):
        """Insert item at a fixed position."""
        heapq.heappush(self.heap, (value, item))

    def extend(self, items):
        """Insert each item in items at its correct position."""
        for item in items:
            self.append(item)

    def fill(self, items, value):
        """Insert each item in items at a fixed position."""
        for item in items:
            self.insert(item, value)

    def pop(self):
        """Pop and return the item (with min or max f(x) value)
        depending on the order."""
        if self.heap:
            return heapq.heappop(self.heap)[1]
        else:
            raise Exception('Trying to pop from empty PriorityQueue.')

    def update(self, item, value):
        del self[item]
        self.insert(item, value)

    def __len__(self):
        """Return current capacity of PriorityQueue."""
        return len(self.heap)

    def __contains__(self, key):
        """Return True if the key is in PriorityQueue."""
        return any([item == key for _, item in self.heap])

    def __getitem__(self, key):
        """Returns the first value associated with key in PriorityQueue.
        Raises KeyError if key is not present."""
        for value, item in self.heap:
            if item == key:
                return value
        raise KeyError(str(key) + " is not in the PriorityQueue.")

    def __delitem__(self, key):
        """Delete the first occurrence of key."""
        try:
            del self.heap[[item == key for _, item in self.heap].index(True)]
        except ValueError:
            raise KeyError(str(key) + " is not in the PriorityQueue.")
        heapq.heapify(self.heap)

class Color(int):
    """Just like 'bool', except values display as 'Black' and 'Red' instead of 'True' and 'False' """
    __str__ = __repr__ = lambda self: 'Black' if self else 'Red'

Black = Color(True)
Red = Color(False)
