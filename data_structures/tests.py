# -*- coding: utf-8 -*-
"""
   Collect all tests for project
"""

import pytest
from linked_list import LinkedList, Node as Node_Linked
from my_queue import Queue, Node as Queue_Node
from stack import Stack, Node as Stack_Node
from hash_table import HashTable, Node as Hash_Node
from binary_search_tree import BinaryTree
from graph import UndirectedGraph, LinkedList as Linked_Graph, Node as Graph_Node


@pytest.fixture(scope="function", name="instance_linked_list")
def create_linked_list():
    linked_list = LinkedList()
    yield linked_list
    del linked_list


@pytest.fixture(scope="function", name="instance_queue")
def create_queue():
    queue = Queue()
    yield queue
    del queue


@pytest.fixture(scope="function", name="instance_stack")
def create_stack():
    stack = Stack()
    yield stack
    del stack


@pytest.fixture(scope="function", name="instance_hash_table")
def create_hash_table():
    hash_table = HashTable(30)
    yield hash_table
    del hash_table


@pytest.fixture(scope="function", name="instance_binary_tree")
def create_binary_tree():
    binary_tree = BinaryTree(50)
    yield binary_tree
    del binary_tree


@pytest.fixture(scope="function", name="instance_graph")
def create_graph():
    linked_list = Linked_Graph()
    linked_list.append(Graph_Node(0))
    linked_list.append(Graph_Node(1))
    linked_list.append(Graph_Node(2))
    linked_list.append(Graph_Node(3))
    linked_list.append(Graph_Node(4))
    graph = UndirectedGraph(5)
    graph.graph = linked_list
    yield graph
    del graph


def test_append_linked_list(instance_linked_list):
    instance_linked_list.append(Node_Linked(1))
    instance_linked_list.append(Node_Linked(2))
    assert instance_linked_list.head.next.data == 2


def test_prepend_linked_list(instance_linked_list):
    instance_linked_list.append(Node_Linked(1))
    instance_linked_list.append(Node_Linked(2))
    instance_linked_list.prepend(Node_Linked(6))
    assert instance_linked_list.head.data == 6


def test_lookup_linked_list(instance_linked_list):
    instance_linked_list.append(Node_Linked(1))
    instance_linked_list.append(Node_Linked(2))
    instance_linked_list.append(Node_Linked(3))
    assert instance_linked_list.lookup(3) == 2
    assert instance_linked_list.lookup(4) is None


def test_delete_linked_list(instance_linked_list):
    instance_linked_list.append(Node_Linked(1))
    instance_linked_list.append(Node_Linked(2))
    instance_linked_list.append(Node_Linked(3))
    instance_linked_list.delete(1)
    assert instance_linked_list.head.next.data == 3


def test_insert_linked_list(instance_linked_list):
    instance_linked_list.insert(Node_Linked(1), 0)
    instance_linked_list.insert(Node_Linked(2), 1)
    instance_linked_list.insert(Node_Linked(3), 2)
    assert instance_linked_list.head.next.data == 2


def test_enqueue_queue(instance_queue):
    instance_queue.enqueue(Queue_Node(1))
    instance_queue.enqueue(Queue_Node(2))
    instance_queue.enqueue(Queue_Node(3))
    assert instance_queue.last.data == 3


def test_dequeue_queue(instance_queue):
    instance_queue.enqueue(Queue_Node(1))
    instance_queue.enqueue(Queue_Node(2))
    instance_queue.enqueue(Queue_Node(3))

    assert instance_queue.dequeue().data == 1
    assert instance_queue.head.data == 2


def test_peek_queue(instance_queue):
    instance_queue.enqueue(Queue_Node(1))
    instance_queue.enqueue(Queue_Node(2))

    assert instance_queue.peek() == 1


def test_push_stack(instance_stack):
    instance_stack.push(Stack_Node(1))
    instance_stack.push(Stack_Node(2))

    assert instance_stack.head.data == 2


def test_pop_stack(instance_stack):
    instance_stack.push(Stack_Node(1))
    instance_stack.push(Stack_Node(2))
    assert instance_stack.pop().data == 2
    assert instance_stack.pop().data == 1
    assert instance_stack.pop() is None


def test_peek_stack(instance_stack):
    instance_stack.push(Stack_Node(1))
    instance_stack.push(Stack_Node(2))
    assert instance_stack.peek().data == 2


def test_insert_hash_table(instance_hash_table):
    instance_hash_table.insert(Hash_Node('first', 1))
    instance_hash_table.insert(Hash_Node('second', 2))

    assert instance_hash_table.linked_list.head.next.value == 2


def test_lookup_hash_table(instance_hash_table):
    instance_hash_table.insert(Hash_Node('first', 1))
    instance_hash_table.insert(Hash_Node('second', 2))

    assert instance_hash_table.lookup('second') == 2


def test_delete_hash_table(instance_hash_table):
    instance_hash_table.insert(Hash_Node('first', 1))
    instance_hash_table.insert(Hash_Node('second', 2))
    instance_hash_table.delete('second')
    assert instance_hash_table.linked_list.head.next is None


def test_insert_binary_tree(instance_binary_tree):
    instance_binary_tree.insert(17)
    instance_binary_tree.insert(72)
    instance_binary_tree.insert(12)
    instance_binary_tree.insert(23)
    assert instance_binary_tree.left.value == 17
    assert instance_binary_tree.right.value == 72
    assert instance_binary_tree.left.left.value == 12
    assert instance_binary_tree.left.right.value == 23


def test_lookup_binary_tree(instance_binary_tree):
    instance_binary_tree.insert(17)
    instance_binary_tree.insert(72)
    instance_binary_tree.insert(12)
    instance_binary_tree.insert(23)
    assert instance_binary_tree.lookup(72) is not None
    assert instance_binary_tree.lookup(100) is None


def test_delete_binary_tree(instance_binary_tree):
    instance_binary_tree.insert(17)
    instance_binary_tree.insert(72)
    instance_binary_tree.insert(12)
    instance_binary_tree.insert(23)
    instance_binary_tree.delete(12)
    assert instance_binary_tree.left.value == 17
    assert instance_binary_tree.right.value == 72
    assert instance_binary_tree.left.right.value == 23
    assert instance_binary_tree.left.left is None


def test_lookup_graph(instance_graph):
    instance_graph.insert(0, 1)
    instance_graph.insert(0, 4)
    instance_graph.insert(1, 2)
    instance_graph.insert(1, 3)
    instance_graph.insert(1, 4)
    instance_graph.insert(2, 3)
    instance_graph.insert(3, 4)
    instance_graph.insert(1, 5)
    assert instance_graph.lookup_vertex(2).vertex == 2
