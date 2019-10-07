"""
Generate random arrays and/or with special behaviour.
Implement insertion_sort.
Implement quick_sort.

Add basic utils.

"""

# TO DO:
# Implement insertion_sort and quick_sort.

from sortedcontainers import SortedList
import numpy as np

# ______________________________________________________________________________

def insertion_sort(data):
    for j in range(1, len(data)):    
        key = data[j]
        i = j - 1
        while i >= 0 and data[i] > key:
            data[i + 1] = data[i]
            i = i - 1
        data[i + 1] = key

# ______________________________________________________________________________

def partition(data,p,r):
    x = data[r]
    i = p - 1
    for j in range(p,r):
        if data[j] <= x:
            i = i + 1
            data[i],data[j] = data[j],data[i]
    data[i + 1],data[r] = data[r],data[i + 1]
    return (i + 1)

def quick_sort(data,p,r):
    if p < r:
        q = partition(data,p,r)
        quick_sort(data,p,q - 1)
        quick_sort(data,q + 1,r)

#______________________________________________________________________________
""" array generation """

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