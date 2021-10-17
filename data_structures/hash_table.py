# -*- coding: utf-8 -*-
"""
   Implements of simple HashTable.
"""


class Node:
    """
    Implement simple Node with key, value, next_node
    """

    def __init__(self, key, value, next_node=None):

        self.key = key
        self.value = value
        self.next = next_node

    def __repr__(self):
        return f'Node {self.key}:{self.value}'

    def __str__(self):
        return f'Node {self.key}:{self.value}'


class LinkedList:
    """
    Implementation of simple LinkedList.
    """
    def __init__(self):
        self.head = None
        self.size = 0

    def __repr__(self):
        return f'Node {self.head.key}:{self.head.value}'

    def __str__(self):
        return f'Node {self.head.key}:{self.head.value}'


class HashTable:
    """
    Implementation of simple HashTable.
    """

    def __init__(self, size):

        self.linked_list = LinkedList()
        self.size = size

    def insert(self, new_node):
        """
        Add item with key to hash table.
        """
        if new_node.key == self.lookup(new_node.key):
            raise KeyError("Hash table contains such key. Please choose other one")

        if self.linked_list.head is None:
            self.linked_list.head = new_node
            self.linked_list.head.key = self.hash_func(new_node.key)
        else:
            last_node = self.linked_list.head
            while last_node.next is not None:
                last_node = last_node.next
            last_node.next = new_node
            last_node.next.key = self.hash_func(new_node.key)

    def hash_func(self, key):
        """
        Count hash.
        """
        hashed_key = 0
        for char in key:
            hashed_key += ord(char)

        return hashed_key % self.size

    def lookup(self, key):
        """
        Get value by key.
        """
        current_head = self.linked_list.head
        hash_key = self.hash_func(key)
        while current_head:
            if current_head.key == hash_key:
                return current_head.value
            current_head = current_head.next

    def delete(self, key):
        """
        Remove value by key
        """
        hash_key = self.hash_func(key)

        current_head = self.linked_list.head
        previous_head = None
        if current_head.key == hash_key:
            self.linked_list.head = current_head.next
        else:
            while current_head.next:
                previous_head = current_head
                current_head = current_head.next
                if current_head.key == hash_key:
                    previous_head.next = current_head.next

    def display(self):
        """
        Display the chain of elements in LinkedList.
        """
        temp_node = self.linked_list.head
        while temp_node is not None:
            print(temp_node.value, ":", temp_node.key,  end='->')
            temp_node = temp_node.next


if __name__ == '__main__':

    hash_table = HashTable(30)
    hash_table.insert(Node('first', 1))
    hash_table.insert(Node('second', 2))
    hash_table.insert(Node('third', 3))
    hash_table.display()
    print()
    print(hash_table.lookup('second'))
    print()
    hash_table.delete('second')
    hash_table.display()
