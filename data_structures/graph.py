# -*- coding: utf-8 -*-
"""
   Implements of simple LinkedList.
"""


class LinkedList:
    """
    Implementation of simple LinkedList.
    """

    def __init__(self):
        self.head = None

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

    def display(self):
        """
        Display the chain of elements in LinkedList.
        """
        temp_node = self.head
        while temp_node is not None:
            print(temp_node.vertex, end='->')
            temp_node = temp_node.next


class Node:
    """
    Implement simple Node with
    """

    def __init__(self, data):
        self.vertex = data
        self.next = None
        self.container = None

    def __repr__(self):
        return f"Node: {self.vertex}"

    def __str__(self):
        return f"Node: {self.vertex}"


class UndirectedGraph:
    """
    Implement simple Undirected Graph
    """

    def __init__(self, vertices):
        self.count_vertices = vertices
        self.graph = None

    def insert(self, source, destination):
        """
        Add a node and links to other nodes by links.
        """

        node = Node(destination)
        node.next = self.lookup(source)
        self.insert_to_list(node, source)
        node = Node(source)
        node.next = self.lookup(destination)
        self.insert_to_list(node, destination)

    def lookup(self, index):
        """
        Find the index of an element by value (first found) and return the index of element or None
        if not found.
        """
        index_counter = 0
        last_node = self.graph.head
        while last_node and index_counter != index:
            last_node = last_node.next
            index_counter += 1
        return last_node.container

    def insert_to_list(self, data, index):
        """
        Insert an element at a specific index with shift elements to the right.
        """
        count = 0
        start_node = self.graph.head
        while count < index:
            start_node = start_node.next
            count += 1

        start_node.container = data

    def display_graph(self):
        """
        Display Graph
        """
        temp = self.graph.head
        for i in range(self.count_vertices):
            print('Adjacency list of vertex {}\n head'.format(i))
            while temp.container:
                print(' -> {}'.format(temp.container.vertex), end="")
                temp.container = temp.container.next
            if temp.next:
                temp = temp.next
            print('\n')

    def lookup_vertex(self, index):
        """
        find a node by value and return a link on him.
        """
        index_counter = 0
        last_node = self.graph.head
        while last_node and index_counter != index:
            last_node = last_node.next
            index_counter += 1
        return last_node


if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.append(Node(0))
    linked_list.append(Node(1))
    linked_list.append(Node(2))
    linked_list.append(Node(3))
    linked_list.append(Node(4))

    graph = UndirectedGraph(5)
    graph.graph = linked_list
    graph.insert(0, 1)
    graph.insert(0, 4)
    graph.insert(1, 2)
    graph.insert(1, 3)
    graph.insert(1, 4)
    graph.insert(2, 3)
    graph.insert(3, 4)
    graph.display_graph()
    print('lookup===========================')
    print(graph.lookup_vertex(2))
