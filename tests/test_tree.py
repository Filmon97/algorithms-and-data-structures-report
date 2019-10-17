import pytest
from tree import (
    BinarySearchTree,
    RedBlackTree
)
from utils import (
    np,SortedList,
    gen_random_u_array,
    gen_reversed_array,
    gen_sorted_array
)

#TODO: add some tests

np.random.seed(31415)

def test_insertion_bst():
    data = gen_random_u_array()
    sorted_data = SortedList(data)

    bst = BinarySearchTree()
    
    for d in data:
        bst.insert(d)

    assert np.array_equal(bst.inorder(),sorted_data)

def test_insertion_rn():
    data = gen_random_u_array()
    sorted_data = SortedList(data)

    rn = RedBlackTree()
    
    for d in data:
        rn.insert(d)
        
    assert np.array_equal(rn.inorder(),sorted_data)




if __name__ == "__main__":
    pytest.main()
