"""
Implement BinarySearchTree.
Implement RedBlackTree.
"""
from utils import (Red,Black)

class Node:
    """A node in a binary search tree. Contains a pointer to the parent (the node
    that this is a successor of).
    extend for red-black tree"""

    def __init__(self, key, parent=None,color=None):
        """Create a Node."""
        self.parent = parent
        self.key = key
        self.left = None
        self.right = None
        if color is not None:
            self.color = color
    def __repr__(self):
        return "<Node {}>".format(self.key)

    def __lt__(self, node):
        return self.key < node.key

    # We want for a queue of nodes in a Tree to have no
    # duplicated key, so we treat nodes with the same
    # value as equal.

    def __eq__(self, other):
        return isinstance(other, Node) and self.key is other.key

    def __hash__(self):
        return hash(self.key)
    
    def child_node(self):
        """Return the left and right nodes """
        children = [] 
        if (self.left is not None):
            children.append(self.left)
        if (self.right is not None): 
            children.append(self.right)
        return children

class BinarySearchTree:
    """Binary Search Tree """

    def __init__(self):
        self.root = None
        
    def insert(self, key):
        self.insert_node(Node(key))

    def insert_node(self, z):
        x = self.root
        y = x
        while x: # x != None
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.p = y
        if y is None:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z
        z.left = None
        z.right = None

    def find(self, key, x=None):
        """Find key-valued node"""
        if x is None:
            x = self.root
        while x and key is not x.key: # x!= None
            if key < x.key:
                x = x.left
            else:
                x = x.right
        return x

    def inorder(self):
        """Inorder returns an array"""
        nodes = []
        def r_inorder(v):
            """Recursive inorder"""
            if(v is None):
                return
            if(v.left is not None):
                r_inorder(v.left)
            nodes.append(v.key)
            if(v.right is not None):
                r_inorder(v.right)
        r_inorder(self.root)
        return nodes
   
    def recursive_height(self,x):
        if x is None:
            return -1
        return max(self.recursive_height(x.left), self.recursive_height(x.right)) + 1

    def tree_height(self):
        return self.recursive_height(self.root)
    
    def minimum(self, x=None):
        if x is None:
            x = self.root
        while x.left is not None:
            x = x.left
        return x

    def maximum(self, x=None):
        if x is None:
            x = self.root
        while x.right is not None:
            x = x.right
        return x

#TODO: remove inheritance
# the code should be implementation-indipendence
# also most of the methods are overridden because
# of self.nil
class RedBlackTree(BinarySearchTree):
    """RedBlackTree """
    def __init__(self):
        self.nil = Node(None, color=Black)
        self.root = self.nil

    def insert(self, key):
        self.insert_node(Node(key, color=Black))
            
    def insert_node(self, z):
        y = self.nil
        x = self.root
        while x is not self.nil:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.p = y
        if y is self.nil:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z
        z.left = self.nil
        z.right = self.nil
        z.color = Red
        self.insert_fixup(z)
        
        
    def insert_fixup(self, z):
        while z.p.color is Red:
            if z.p is z.p.p.left:
                y = z.p.p.right
                if y.color is Red:
                    z.p.color = Black
                    y.color = Black
                    z.p.p.color = Red
                    z = z.p.p
                else:
                    if z is z.p.right:
                        z = z.p
                        self.left_rotate(z)
                    z.p.color = Black
                    z.p.p.color = Red
                    self.right_rotate(z.p.p)
            else:
                y = z.p.p.left
                if y.color is Red:
                    z.p.color = Black
                    y.color = Black
                    z.p.p.color = Red
                    z = z.p.p
                else:
                    if z is z.p.left:
                        z = z.p
                        self.right_rotate(z)
                    z.p.color = Black
                    z.p.p.color= Red
                    self.left_rotate(z.p.p)
        self.root.color = Black

    
    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left is not self.nil:
            y.left.p = x
        y.p = x.p
        if x.p is self.nil:
            self.root = y
        elif x is x.p.left:
            x.p.left = y
        else:
            x.p.right = y
        y.left = x
        x.p = y

    def right_rotate(self, y):
        x = y.left
        y.left = x.right
        if x.right is not self.nil:
            x.right.p = y
        x.p = y.p
        if y.p is self.nil:
            self.root = x
        elif y is y.p.right:
            y.p.right = x
        else:
            y.p.left = x
        x.right = y
        y.p = x
    
    def inorder(self):
        """Inorder returns an array"""
        nodes = []
        def r_inorder(v):
            """Recursive inorder"""
            if(v is self.nil):
                return
            if(v.left is not self.nil):
                r_inorder(v.left)
            nodes.append(v.key)
            if(v.right is not self.nil):
                r_inorder(v.right)
        r_inorder(self.root)
        return nodes
    
    def postorder(self):
        """Postorder returns an array"""
        nodes = []
        def r_postorder(v):
            """Recursive postorder"""
            if(v is self.nil):
                return
            if(v.left is not self.nil):
                r_postorder(v.left)
            if(v.right is not self.nil):
                r_postorder(v.right)
            nodes.append(v.key)
        r_postorder(self.root)
        return nodes