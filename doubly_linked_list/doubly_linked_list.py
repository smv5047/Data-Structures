"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""

    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""

    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it
    as the new head of the list. Don't forget to handle
    the old head node's previous pointer accordingly."""

    #   head will not have previous, tail will not have next
    def add_to_head(self, value):
        if self.length == 0:
            new_node = ListNode(value)
            self.head = new_node
            self.tail = new_node

        else:
            # create node and insert before current head
            self.head.insert_before(value)
            # set the head of the dll to the head to what is before the old head
            self.head = self.head.prev
        # add to dll length
        self.length += 1

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""

    def remove_from_head(self):
        if self.length == 0:
            return None
        elif self.length == 1:
            # make self.head.next the head
            # self.head.next = self.head
            # # make new head have no previous
            # self.head.prev = None
            removed_node = self.head
            # new_head_node = self.head.next
            self.head.delete()
            self.head = None
            self.tail = None
            self.length -= 1
            # self.head = new_head_node
            return removed_node.value
        else:
            # make self.head.next the head
            # self.head.next = self.head
            # # make new head have no previous
            # self.head.prev = None
            removed_node = self.head
            # new_head_node = self.head.next
            self.head.delete()
            self.length -= 1
            # self.head = new_head_node
            return removed_node.value

    """Wraps the given value in a ListNode and inserts it
    as the new tail of the list. Don't forget to handle
    the old tail node's next pointer accordingly."""

    def add_to_tail(self, value):
        if self.length == 0:
            new_node = ListNode(value)
            new_node.next = None
            new_node.prev = None
            self.head = new_node
            self.tail = new_node
            self.length += 1
        else:

            # insert new node
            self.tail.insert_after(value)
            # reassign tail node
            self.tail = self.tail.next
            # add to length
            self.length += 1

    """Removes the List's current tail node, making the
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""

    def remove_from_tail(self):
        if self.length == 0:
            return None
        elif self.length == 1:
            old_tail = self.tail
            self.tail.delete()
            self.head = None
            self.tail = None
            self.length -= 1
            return old_tail.value
        else:
            old_tail = self.tail
            self.tail.delete()
            self.length -= 1
            return old_tail.value

    """Removes the input node from its current spot in the
    List and inserts it as the new head node of the List."""

    def move_to_front(self, node):
        # TODO - Discuss why node.delete() will not work for this and move_to_end
        if self.length == 0:
            return
        elif self.length == 1:
            return
        else:
            if node == self.head:
                return
            else:
                moving_node = node.value
                self.delete(node)
                # node.delete()
                self.add_to_head(moving_node)

    """Removes the input node from its current spot in the
    List and inserts it as the new tail node of the List."""

    def move_to_end(self, node):
        if self.length == 0:
            return
        elif self.length == 1:
            return
        else:
            if node == self.tail:
                return
            else:
                moving_node = node.value
                self.delete(node)
                # node.delete()
                self.add_to_tail(moving_node)

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""

    def delete(self, node):
        if self.length == 0:
            return None
        elif self.length == 1:
            node.delete()
            self.head = None
            self.tail = None
        elif node == self.head:
            new_head = self.head.next
            node.delete()
            self.head = new_head
        elif node == self.tail:
            new_tail = self.tail.prev
            node.delete()
            self.tail = new_tail
        else:
            node.delete()
        self.length -= 1

    """Returns the highest value currently in the list"""

    def get_max(self):
        if self.length == 0:
            return
        elif self.length == 1:
            return self.head.value
        else:
            # set 1st value as max
            max_num = self.head.value
            current_node = self.head
            while current_node:
                if current_node.value > max_num:
                    max_num = current_node.value
                current_node = current_node.next
            return max_num

        # if there is an additional node, check that value


new_dll = DoublyLinkedList(ListNode(5))
# print(new_dll.head.value)
new_dll.remove_from_head()
# print(new_dll.head.value)
print(len(new_dll))
