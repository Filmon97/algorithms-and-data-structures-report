"""
Implement insertion_sort.
Implement quick_sort.
"""
from utils import jit
# ______________________________________________________________________________
@jit
def insertion_sort(data):
    for j in range(1, len(data)):
        key = data[j]
        i = j - 1
        while i >= 0 and data[i] > key:
            data[i + 1] = data[i]
            i = i - 1
        data[i + 1] = key


# ______________________________________________________________________________

@jit
def partition(data, p, r):
    x = data[r]
    i = p - 1
    for j in range(p, r):
        if data[j] <= x:
            i = i + 1
            data[i], data[j] = data[j], data[i]
    data[i + 1], data[r] = data[r], data[i + 1]
    return i + 1

@jit
def quick_sort(data, p, r):
    if p < r:
        q = partition(data, p, r)
        quick_sort(data, p, q - 1)
        quick_sort(data, q + 1, r)
