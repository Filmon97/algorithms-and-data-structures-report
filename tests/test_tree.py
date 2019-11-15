import pytest
from tree import (
    BinarySearchTree,
    RedBlackTree,
    Red, Black
)
from utils import (
    np, SortedList,
    gen_random_u_array,
    gen_sorted_array
)

np.random.seed(31415)


def test_insert():
    bst = BinarySearchTree()
    rbt = RedBlackTree()

    bst.insert(5)
    rbt.insert(5)

    assert bst.find(5) and rbt.find(5)

# FIXME
def test_insert_fixup():
    rbt = RedBlackTree()

    rbt.insert(5)
    rbt.insert(6)
    rbt.insert(2)

    assert rbt.root.color is Black and rbt.root.left.color \
        is Red and rbt.root.right.color is Red and rbt.nil.color is Black


def test_find():
    bst = BinarySearchTree()
    rbt = RedBlackTree()

    assert bst.find(5) is None and rbt.find(5) is None


def test_inorder():
    bst = BinarySearchTree()
    rbt = RedBlackTree()
    data = gen_random_u_array(10)

    for d in data:
        bst.insert(d)
        rbt.insert(d)

    assert np.array_equal(bst.inorder(), rbt.inorder())


def test_tree_height():
    bst = BinarySearchTree()
    rbt = RedBlackTree()
    data = gen_random_u_array()

    for d in data:
        bst.insert(d)
        rbt.insert(d)

    assert bst.tree_height() is not rbt.tree_height()


def test_minimum():
    bst = BinarySearchTree()
    rbt = RedBlackTree()
    data = gen_random_u_array(10)

    for d in data:
        bst.insert(d)
        rbt.insert(d)

    assert bst.minimum().key is rbt.minimum().key


def test_maximum():
    bst = BinarySearchTree()
    rbt = RedBlackTree()
    data = gen_random_u_array(10)

    for d in data:
        bst.insert(d)
        rbt.insert(d)

    assert bst.maximum().key is rbt.maximum().key

# TODO


def test_left_rotate():
    pass


def test_right_rotate():
    pass


def test_postorder():
    bst = BinarySearchTree()
    rbt = RedBlackTree()
    data = gen_random_u_array(10)

    for d in data:
        bst.insert(d)
        rbt.insert(d)

    assert np.array_equal(bst.postorder(), rbt.postorder()) is False


def test_insertion_bst():
    data = gen_random_u_array()
    sorted_data = SortedList(data)

    bst = BinarySearchTree()

    for d in data:
        bst.insert(d)

    assert np.array_equal(bst.inorder(), sorted_data)


def test_insertion_rn():
    data = gen_random_u_array()
    sorted_data = SortedList(data)

    rbt = RedBlackTree()

    for d in data:
        rbt.insert(d)

    assert np.array_equal(rbt.inorder(), sorted_data)


if __name__ == "__main__":
    pytest.main()
