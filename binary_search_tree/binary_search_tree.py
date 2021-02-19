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
#############


class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node


class LinkedList:
    def __init__(self):
        self.head = None  # Stores a node, that corresponds to our first node in the list
        self.tail = None  # stores a node that is the end of the list

    def add_to_head(self, value):
        # create a node to add
        new_node = Node(value)
        # check if list is empty
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            # new_node should point to current head
            new_node.next_node = self.head
            # move head to new node
            self.head = new_node

    def add_to_tail(self, value):
        # create a node to add
        new_node = Node(value)
        # check if list is empty
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            # point the node at the current tail, to the new node
            self.tail.next_node = new_node
            self.tail = new_node

    # remove the head and return its value
    def remove_head(self):
        # if list is empty, do nothing
        if not self.head:
            return None
        # if list only has one element, set head and tail to None
        if self.head.next_node is None:
            head_value = self.head.value
            self.head = None
            self.tail = None
            return head_value
        # otherwise we have more elements in the list
        head_value = self.head.value
        self.head = self.head.next_node
        return head_value

    def contains(self, value):
        if self.head is None:
            return False

        # Loop through each node, until we see the value, or we cannot go further
        current_node = self.head

        while current_node is not None:
            # check if this is the node we are looking for
            if current_node.value == value:
                return True

            # otherwise, go to the next node
            current_node = current_node.next_node
        return False


class Queue:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.size += 1
        self.storage.add_to_tail(value)

    def dequeue(self):
        if self.size > 0:
            self.size -= 1
            return self.storage.remove_head()
        else:
            return None


##############

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            # if no self.left exist, make self.left = value
            if self.left is not None:
                self.left.insert(value)
            else:
                self.left = BSTNode(value)
        if value >= self.value:
            if self.right is not None:
                self.right.insert(value)
            else:
                self.right = BSTNode(value)

    def contains(self, target):
        if self.value == target:
            return True
        if self.value > target:
            if self.left is None:
                return False
            found = self.left.contains(target)
        else:
            if self.right is None:
                return False
            found = self.right.contains(target)
        return found

    # Return the maximum value found in the tree

    def get_max(self):

        if self.right is None:
            return self.value
        return self.right.get_max()

    # Call the function `fn` on the value of each node

    def for_each(self, fn):
        if self.value is None:
            return
        if self.value is not None:
            fn(self.value)
        if self.right is not None:
            self.right.for_each(fn)
        if self.left is not None:
            self.left.for_each(fn)
        # highlight current node
        # if it exists call function on it
        # if it has a right or left node, make those call a function on them

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal

    def in_order_print(self, node):

        if self.value is None:
            return
        if self.left:
            self.left.in_order_print(self.value)
        print(self.value)
        if self.right:
            self.right.in_order_print(self.value)

        # Print the value of every node, starting with the given node,
        # in an iterative breadth first traversal

    def bft_print(self, node):

        # create a queu for nodes
        queue = Queue()
        # add the first node to the queue
        queue.enqueue(node)
        # while queue is not empty
        while len(queue) > 0:
            # remove the first node from the queue
            removed_node = queue.dequeue()
        # print the removed node
            print(removed_node.value)
        # add all children into the queue (first children of 8 then of 3
            if removed_node.left:
                queue.enqueue(removed_node.left)

            if removed_node.right:
                queue.enqueue(removed_node.right)

        # Print the value of every node, starting with the given node,
        # in an iterative depth first traversal

    def dft_print(self, node):

        # create a stocak for nodes
        stack = []
        # add the first node to the stack
        stack.append(node)
        # while the stack is not empty
        while len(stack) > 0:
            # get the current node from the top of the stack
            removed_node = stack.pop()
            # print that node
            print(removed_node.value)
            # add all children to the stack (add right side first since it's bigger)
            if removed_node.right:
                stack.append(removed_node.right)
            if removed_node.left:
                stack.append(removed_node.left)
            # keep in mind the order you add the children will matter

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass


root = BSTNode(5)
root.insert(30)
root.insert(17)
root.insert(11)
print(root.in_order_print(root))
print(root.dft_print(root))
