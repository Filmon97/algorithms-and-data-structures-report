# algorithm-and-data-structure-reports
Simple reports that analyze insertion and quick sort, search tree, red-black tree, connected components and MST Prim.
Heavily based on *[Introduction to Algorithms Third Edition, published by Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, and Clifford Stein.[CLRS]](https://mitpress.mit.edu/books/introduction-algorithms-third-edition)*
and *[Artificial Intelligence: A Modern Approach](http://aima.cs.berkeley.edu).*
For the python code i also checked the repository: *[aimacode](https://github.com/aimacode/aima-python).*
## Installation Guide

Navigate in the **Anaconda Prompt** and select your environment for example:
`conda activate pyenv`

To download the repository:

`git clone https://github.com/Filmon97/algorithm-and-data-structure-reports.git`

Then you need to install the basic dependencies to run the project on your system:
`pip install -r requirements.txt`

### Visual Studio Code
While you are in the **Anaconda Prompt** run:
`code .`
to open the project in **Visual Studio Code**

If you want to run the test suite:

`pip install pytest`

Then to run the tests:

`pytest`

# Index of Algorithms

Here is a table of the implemented algorithms, the name of the implementation in the repository, and the file where they are implemented.

<!-- [`sort.py`] --->
| **Name** | **File** | **Tests** | **Notebook**
|:------------------------------|:--------------------------------|:-----|:---------|
| `insertion_sort`| [`sort.py`][sort]      | Done | Done |
| `quick_sort`| [`sort.py`][sort]      | Done | Done |

<!-- [`tree.py`] --->
| **Name** | **File** | **Tests** | **Notebook**
|:------------------------------|:--------------------------------|:-----|:---------|
| `insert_node`| [`tree.py`][tree]      | TODO | TODO |
| `insert_fixup`| [`tree.py`][tree]      | TODO | TODO |
| `find`| [`tree.py`][tree]      | TODO | TODO |
| `inorder`| [`tree.py`][tree]      | TODO | TODO |
| `tree_height`| [`tree.py`][tree]      | TODO | TODO |
| `minimum`| [`tree.py`][tree]      | TODO | TODO |
| `maximum`| [`tree.py`][tree]      | TODO | TODO |
| `left_rotate`| [`tree.py`][tree]      | TODO | TODO |
| `right_rotate`| [`tree.py`][tree]      | TODO | TODO |
| `postorder`| [`tree.py`][tree]      | TODO | TODO |


<!-- [`graph.py`] --->
| **Name** | **File** | **Tests** | **Notebook**
|:------------------------------|:--------------------------------|:-----|:---------|
| `connected_components`| [`graph.py`][graph]      | TODO | TODO |
| `mst_prim`| [`graph.py`][graph]      | TODO | TODO |

# Index of Data Structures

Here is a table of the implemented data structures, the name of the implementation in the repository, and the file where they are implemented.

<!-- [`tree.py`] --->
| **Name** | **File** | **Tests** | **Notebook**
|:------------------------------|:--------------------------------|:-----|:---------|
| `Node`| [`tree.py`][tree]      | TODO | TODO |
| `BinarySearchTree`| [`tree.py`][tree]      | TODO | TODO |
| `RedBlackTree`| [`tree.py`][tree]      | TODO | TODO |

<!-- [`graph.py`] --->
| **Name** | **File** | **Tests** | **Notebook**
|:------------------------------|:--------------------------------|:-----|:---------|
| `Graph`| [`graph.py`][graph]      | TODO | TODO |

<!-- [`utils.py`] --->
| **Name** | **File** | **Tests** | **Notebook**
|:------------------------------|:--------------------------------|:-----|:---------|
| `PriorityQueue`| [`utils.py`][utils]      | TODO | TODO |

<!---Reference Links-->
[sort]:../master/sort.py
[tree]:../master/tree.py
[graph]:../master/graph.py
[utils]:../master/utils.py