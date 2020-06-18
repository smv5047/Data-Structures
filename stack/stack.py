"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""


class Stack:
    def __init__(self, size, storage=[]):
        self.size = 0
        self.storage = storage

    def __len__(self):
        stack_length = 0
        for num in self.storage:
            stack_length += 1
        return stack_length

    def push(self, value):
        self.storage.append(value)

    def pop(self):
        length = self.__len__()
        popped = self.storage[length-1]
        del self.storage[:-1]
        return popped


new_stack = Stack(2, [4, 7])

new_stack.push(8)
new_stack.pop()
print(new_stack.__len__())
