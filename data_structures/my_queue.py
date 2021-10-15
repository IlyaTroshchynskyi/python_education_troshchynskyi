# -*- coding: utf-8 -*-
"""
   Implements of simple Queue.
"""


class Node:
    """
    Implement simple Node with data and link to the next node
    """
    def __init__(self, data):

        self.data = data
        self.next = None

    def __repr__(self):
        return f'Node {self.data}'

    def __str__(self):
        return f'Node {self.data}'


class Queue:
    """
    Implementation of simple Queue with link to head and last node
    """

    def __init__(self):
        self.head = None
        self.last = None

    def enqueue(self, new_node):
        """
        Insert an item to the end of the queue
        """
        if self.last is None:
            self.head = new_node
            self.last = self.head
        else:
            self.last.next = new_node
            self.last = self.last.next

    def dequeue(self):
        """
        Remove an item from the head of the queue
        """

        if self.last is None:
            return None
        returned_node = self.head
        self.head = self.head.next
        return returned_node

    def display(self):
        """
        Display the chain of elements in Queue.
        """
        temp_node = self.head
        while temp_node is not None:
            print(temp_node.data, end='->')
            temp_node = temp_node.next

    def peek(self):
        """
        Get the value of the element at the head of the queue.
        """
        return self.head.data


if __name__ == '__main__':
    my_queue = Queue()
    my_queue.enqueue(Node(1))
    my_queue.enqueue(Node(2))
    my_queue.enqueue(Node(3))
    my_queue.display()
    my_queue.dequeue()
    print()
    my_queue.display()
    print()
    print(my_queue.peek())
