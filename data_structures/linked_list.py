# -*- coding: utf-8 -*-
"""
   Implements of simple LinkedList.
"""


class Node:
    """
    Implement simple Node with data
    """

    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f"Node: {self.data}"

    def __str__(self):
        return f"Node: {self.data}"


class LinkedList:
    """
    Implementation of simple LinkedList.
    """

    def __init__(self):
        self.head = None

    def prepend(self, new_node):
        """
        Insert element in LinkedList to the beginning.
        """

        if self.head:
            previous_head = self.head
            self.head = new_node
            self.head.next = previous_head
        else:
            self.head = new_node

    def append(self, new_node):
        """
        Insert element in the LinkedList at the end.
        """

        if self.head:
            last_node = self.head
            while last_node.next is not None:
                last_node = last_node.next

            last_node.next = new_node
        else:
            self.head = new_node

    def lookup(self, value):
        """
        Find the index of an element by value (first found) and return the index of element or None
        if not found.
        """
        index = 0
        last_node = self.head
        while last_node and last_node.data != value:
            last_node = last_node.next
            index += 1
        return None if last_node is None else index

    def display(self):
        """
        Display the chain of elements in LinkedList.
        """
        temp_node = self.head
        while temp_node is not None:
            print(temp_node.data, end='->')
            temp_node = temp_node.next

    def insert(self, data, index):
        """
        Insert an element at a specific index with shift elements to the right.
        """
        if index > 0 and self.head is None:
            raise IndexError("Your index exceed length of linked list")
        if index == 0:
            next_node = self.head
            self.head = data
            self.head.next = next_node
        count = 0
        start_node = self.head
        while count < index-1 and start_node is not None:
            start_node = start_node.next
            count += 1
        temp_node = data
        temp_node.next = start_node.next
        start_node.next = temp_node

    def delete(self, index):
        """
        Remove element by index
        """
        count = 0
        start_node = self.head
        prev_node = None
        if index == 0:
            self.head = start_node.next
            return
        while count < index and start_node is not None:
            prev_node = start_node
            start_node = start_node.next
            count += 1

        prev_node.next = start_node.next
        del start_node


if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.append(Node(1))
    linked_list.append(Node(2))
    linked_list.append(Node(3))
    linked_list.append(Node(4))
    linked_list.append(Node(5))
    linked_list.append(Node(6))
    linked_list.append(Node(7))
    linked_list.prepend(Node(0))
    print(linked_list.lookup(10))
    print(linked_list.lookup(0))
    linked_list.insert(Node(33), 4)
    linked_list.delete(4)
    linked_list.display()
