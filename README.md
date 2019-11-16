# algorithms-and-data-structures-report
Simple reports that analyze insertion and quick sort, search tree, red-black tree, connected components and MST Prim.

The report is based on three exercises assigned by the Professor.

## Exercise 1:
Write one or more Python programs to:
Generate a random array with suitable behaviour
* Implement Insertion Sort algorithm
*  Implement Quick Sort or Merge Sort algorithm

Write a program that performs tests by measuring execution times of the previous algorithms on:
* Sets of data of increasing size(array with 10,100,1000 ... data) 
* With randomly generated input data and sets of data that represent the best/worst cases for an algorithm

## Exercise A
We want to analyze the differences between Binary Search Trees and Red Black Trees
To do this, we'll have to:
* Write Python programs that implement RB tree from the BS tree's code that we saw during class.
    * * Probably the BS tree's implementation that we saw during class should be completed with missing methods or attributes
    * * For the RB trees is not mandatory to consider the deletion (insertion is mandatory)

* Write the programs that execute some tests (experiments) that will help us to understand the advantages and disadvantages of BS trees 

## Exercise F:
Write the below programs to study the algorithm for finding the connected components:

* Randomly generated graphs with an arbitrary nodes cardinality and a given probability of existance of edges(for example given a adj matrix with all zeros, change value to 1 with a given probability)
* Randomly generated weighted graphs
* Finding of connencted components
* Prim's algorithm
* Priority queue data structure (with min-hash)
* A program that conducts experiment on random graphs with a growing dimension and edge presence


Heavily based on *[Introduction to Algorithms Third Edition, published by Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, and Clifford Stein.[CLRS]](https://mitpress.mit.edu/books/introduction-algorithms-third-edition)*
and *[Artificial Intelligence: A Modern Approach](http://aima.cs.berkeley.edu).*
For the Python code I was also inspired by the repository: *[aimacode](https://github.com/aimacode/aima-python).*
## Installation Guide

Navigate in the **Anaconda Prompt** and select your environment for example:
`conda activate pyenv`

To download the repository:

`git clone https://github.com/Filmon97/algorithms-and-data-structures-report.git`

Then you need to install the basic dependencies to run the project on your system:

`pip install -r requirements.txt`


*(This is only for me)* To read the report you will need to fetch the LaTeX code from the overleaf repository *(You don't have the creds)*:

`cd algorithms-and-data-structures-report`

`git submodule init`

`git submodule update`

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


| **Name** | **File** | **Tests**
|:------------------------------|:--------------------------------|:------|
| `insertion_sort`| [`sort.py`][sort]      | Done |<!-- [`sort.py`] --->
| `quick_sort`| [`sort.py`][sort]      | Done |
| `insert`| [`tree.py`][tree]      | Done |<!-- [`tree.py`] --->
| `insert_fixup`| [`tree.py`][tree]      | Done |
| `find`| [`tree.py`][tree]      | Done |
| `inorder`| [`tree.py`][tree]      | Done |
| `tree_height`| [`tree.py`][tree]      | Done |
| `minimum`| [`tree.py`][tree]      | Done |
| `maximum`| [`tree.py`][tree]      | Done |
| `left_rotate`| [`tree.py`][tree]      | TODO |
| `right_rotate`| [`tree.py`][tree]      | TODO |
| `postorder`| [`tree.py`][tree]      | Done |
| `connected_components`| [`graph.py`][graph]      | Done |<!-- [`graph.py`] --->
| `mst_prim`| [`graph.py`][graph]      | Done |

# Index of Data Structures

Here is a table of the implemented data structures, the name of the implementation in the repository, and the file where they are implemented.


| **Name** | **File** | **Tests** 
|:------------------------------|:--------------------------------|:------|
| `Node`| [`tree.py`][tree]      | Done |<!-- [`tree.py`] --->
| `BinarySearchTree`| [`tree.py`][tree]      | Done |
| `RedBlackTree`| [`tree.py`][tree]      | Done |
| `Graph`| [`graph.py`][graph]      | Done |<!-- [`graph.py`] --->
| `PriorityQueue`| [`utils.py`][utils]      | Done |<!-- [`utils.py`] --->

<!---Reference Links-->
[sort]:../master/sort.py
[tree]:../master/tree.py
[graph]:../master/graph.py
[utils]:../master/utils.py
