import pytest
from sort import (
    insertion_sort,
    quick_sort,
)
from utils import (
    np,SortedList,
    gen_random_u_array,
    gen_reversed_array,
    gen_sorted_array
)

# some alternative seeds that can be used with random.seed (non numpy version)
# golden_ratio = (1 + math.sqrt(5))/2
# 'algorithms-and-data-structures-report'
# math.pi or math.e
# 'filmon_arefayne'

np.random.seed(31415)

def test_avg_case_insertion_sort():
    data = gen_random_u_array()
    sorted_data = SortedList(data)

    insertion_sort(data)
    
    assert np.array_equal(data,sorted_data)

def test_avg_case_quick_sort():
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

def test_best_case_insertion_sort():
    data = gen_sorted_array()
    sorted_data = SortedList(data)

    insertion_sort(data)
    
    assert np.array_equal(data,sorted_data)


if __name__ == "__main__":
    pytest.main()
