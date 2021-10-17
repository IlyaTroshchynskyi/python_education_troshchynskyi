# -*- coding: utf-8 -*-
"""
   Implements of simple Stack.
"""


class Node:
    """
    Implement simple Node with data and link to the next node.
    """

    def __init__(self, data):

        self.data = data
        self.next = None

    def __repr__(self):
        return f'Node {self.data}'

    def __str__(self):
        return f'Node {self.data}'


class Stack:

    """
    Implementation of simple Stack with link to head.
    """

    def __init__(self):
        self.head = None

    def push(self, new_node):
        """
        Add item to stack.
        """
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def pop(self):
        """
        Take the last item.
        """

        if self.head is not None:
            returned_node = self.head
            self.head = self.head.next
            return returned_node
        return None

    def display(self):
        """
        Display the chain of elements in Stack.
        """

        temp_node = self.head
        while temp_node is not None:
            print(temp_node.data, end='->')
            temp_node = temp_node.next

    def peek(self):
        """
        Get the value of the last item of the stack.
        """
        return self.head


if __name__ == '__main__':
    my_stack = Stack()
    my_stack.push(Node(1))
    my_stack.push(Node(2))
    my_stack.push(Node(3))
    my_stack.display()
    print()
    print(my_stack.pop())
    print(my_stack.display())
    print(my_stack.peek())
