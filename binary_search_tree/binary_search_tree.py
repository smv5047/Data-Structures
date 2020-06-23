"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        pass
    # root = BSTNode(8)
    # have tree with root 8, if insert node with value 3 insert left

    # if new value < self.value:
        # if self.left is already taken by a node
        # make that (left) node call insert
        # set the left to the new node with the new value

    # if new value >= self.value:
        # if self.right is already taken by a node
        # make that (right) node call insert
        # set the right to the the new node with th enew value

    # Return True if the tree contains the value
    # False if it does not

    def contains(self, target):

        if self.value == target:
            return True

        found = False
        if self.value < target:
            if self.left is None:
                return False
            found = self.left.contains(target)
        # compare the target to current value
        # if current value of node <= target
            # check the left subtree
            # if you cannot go left, return False
        # if current value of node > target
        if self.value > target:
            # check right subtree contains target
            # if you cannot go right, returtn False
            if self.right is None:
                return False
            found = self.right.contains(target)

        return found

    # Return the maximum value found in the tree
    def get_max(self):
        pass

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        pass

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
