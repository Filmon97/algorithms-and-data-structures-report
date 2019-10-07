import pytest
from sort import (
    insertion_sort,
    quick_sort,
    np,SortedList,
    gen_random_u_array,
    gen_reversed_array,
    gen_sorted_array
)
import math

golden_ratio = (1 + math.sqrt(5))/2
 

np.random.seed(golden_ratio)

def test_insertion_sort():
    data = gen_random_u_array()
    sorted_data = SortedList(data)

    insertion_sort(data)
    
    assert np.array_equal(data,sorted_data)

def test_quick_sort():
    data = gen_random_u_array()
    sorted_data = SortedList(data)

    quick_sort(data,0,len(data)-1)

    assert np.array_equal(data,sorted_data)

def test_worst_case_insertion_sort():
    data = gen_reversed_array()
    sorted_data = SortedList(data)
    
    insertion_sort(data)
    
    assert np.array_equal(data,sorted_data)

def test_worst_case_quick_sort():
    data = gen_sorted_array()
    sorted_data = SortedList(data)

    quick_sort(data,0,len(data)-1)

    assert np.array_equal(data,sorted_data)

if __name__ == "__main__":
    pytest.main()