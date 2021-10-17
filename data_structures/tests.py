# -*- coding: utf-8 -*-
"""
   Collect all tests for project
"""

import random
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


@pytest.mark.parametrize("number_1, number_2", [(random.randint(1, 100), random.randint(1, 100))
                                                for _ in range(100)])
def test_append_linked_list(instance_linked_list, number_1, number_2):
    instance_linked_list.append(Node_Linked(number_1))
    instance_linked_list.append(Node_Linked(number_2))
    assert instance_linked_list.head.next.data == number_2


@pytest.mark.parametrize("number", [random.randint(1, 100) for _ in range(100)])
def test_prepend_linked_list(instance_linked_list, number):
    instance_linked_list.append(Node_Linked(1))
    instance_linked_list.append(Node_Linked(2))
    instance_linked_list.prepend(Node_Linked(number))
    assert instance_linked_list.head.data == number


@pytest.mark.parametrize("number", [random.randint(4, 100) for _ in range(100)])
def test_lookup_linked_list(instance_linked_list, number):
    instance_linked_list.append(Node_Linked(1))
    instance_linked_list.append(Node_Linked(2))
    instance_linked_list.append(Node_Linked(number))
    assert instance_linked_list.lookup(number) == 2
    assert instance_linked_list.lookup(number+100) is None


@pytest.mark.parametrize("number_1, number_2", [(x+4, x+104) for x in range(100)])
def test_delete_linked_list(instance_linked_list, number_1, number_2):
    instance_linked_list.append(Node_Linked(500))
    instance_linked_list.append(Node_Linked(number_1))
    instance_linked_list.append(Node_Linked(1000))
    instance_linked_list.append(Node_Linked(number_2))
    instance_linked_list.delete(1)
    assert instance_linked_list.head.next.data == 1000


@pytest.mark.parametrize("number", [random.randint(0, 6) for x in range(20)])
def test_insert_linked_list(instance_linked_list, number):
    instance_linked_list.insert(Node_Linked(1), 0)
    instance_linked_list.insert(Node_Linked(2), 1)
    instance_linked_list.insert(Node_Linked(3), 2)
    instance_linked_list.insert(Node_Linked(4), 3)
    instance_linked_list.insert(Node_Linked(5), 4)
    instance_linked_list.insert(Node_Linked(6), 5)
    instance_linked_list.insert(Node_Linked(7), 6)
    instance_linked_list.insert(Node_Linked(number+20), number)
    assert instance_linked_list.lookup(number+20) == number


@pytest.mark.parametrize("number", [random.randint(1, 1000) for _ in range(100)])
def test_enqueue_queue(instance_queue, number):
    instance_queue.enqueue(Queue_Node(1))
    instance_queue.enqueue(Queue_Node(2))
    instance_queue.enqueue(Queue_Node(number))
    assert instance_queue.last.data == number


@pytest.mark.parametrize("number", [random.randint(1, 1000) for _ in range(100)])
def test_dequeue_queue(instance_queue, number):
    instance_queue.enqueue(Queue_Node(number))
    instance_queue.enqueue(Queue_Node(2))
    instance_queue.enqueue(Queue_Node(3))
    assert instance_queue.dequeue().data == number
    assert instance_queue.head.data == 2


@pytest.mark.parametrize("number", [random.randint(1, 1000) for _ in range(100)])
def test_peek_queue(instance_queue, number):
    instance_queue.enqueue(Queue_Node(number))
    instance_queue.enqueue(Queue_Node(2))
    assert instance_queue.peek() == number


@pytest.mark.parametrize("number_1, number_2", [(random.randint(1, 100), random.randint(1, 100))
                                                for _ in range(100)])
def test_push_stack(instance_stack, number_1, number_2):
    instance_stack.push(Stack_Node(number_1))
    instance_stack.push(Stack_Node(number_2))
    assert instance_stack.head.data == number_2


@pytest.mark.parametrize("number_1, number_2", [(random.randint(1, 100), random.randint(1, 100))
                                                for _ in range(100)])
def test_pop_stack(instance_stack, number_1, number_2):
    instance_stack.push(Stack_Node(number_1))
    instance_stack.push(Stack_Node(number_2))
    assert instance_stack.pop().data == number_2
    assert instance_stack.pop().data == number_1
    assert instance_stack.pop() is None


@pytest.mark.parametrize("number_1, number_2", [(random.randint(1, 100), random.randint(1, 100))
                                                for _ in range(100)])
def test_peek_stack(instance_stack, number_1, number_2):
    instance_stack.push(Stack_Node(number_1))
    instance_stack.push(Stack_Node(number_2))
    assert instance_stack.peek().data == number_2


@pytest.mark.parametrize("key, number", [('third', 3), ('forth', 4), ('fifth', 5),
                                         ('sixth', 6), ('seventh', 7), ('eighth', 8),
                                         ('ninth', 9), ('tenth', 10)])
def test_insert_hash_table(instance_hash_table, key, number):

    instance_hash_table.insert(Hash_Node('first', 1))
    instance_hash_table.insert(Hash_Node('second', 2))
    instance_hash_table.insert(Hash_Node(key, number))
    assert number == instance_hash_table.lookup(key)


@pytest.mark.parametrize("key, number", [('third', 3), ('forth', 4), ('fifth', 5),
                                         ('sixth', 6), ('seventh', 7), ('eighth', 8),
                                         ('ninth', 9), ('tenth', 10)])
def test_lookup_hash_table(instance_hash_table, key, number):
    instance_hash_table.insert(Hash_Node('first', 1))
    instance_hash_table.insert(Hash_Node('second', 2))
    instance_hash_table.insert(Hash_Node(key, number))
    assert instance_hash_table.lookup(key) == number


@pytest.mark.parametrize("key, number", [('third', 3), ('forth', 4), ('fifth', 5),
                                         ('sixth', 6), ('seventh', 7), ('eighth', 8),
                                         ('ninth', 9), ('tenth', 10)])
def test_delete_hash_table(instance_hash_table, key, number):
    instance_hash_table.insert(Hash_Node('first', 1))
    instance_hash_table.insert(Hash_Node(key, number))
    instance_hash_table.delete(key)
    assert instance_hash_table.linked_list.head.next is None


@pytest.mark.parametrize("number_1, number_2, number_3, number_4",
                         [(17, 72, 12, 23), (18, 73, 13, 24),
                          (19, 74, 14, 25), (20, 75, 15, 26),
                          (21, 76, 16, 27), (22, 77, 17, 28)])
def test_insert_binary_tree(instance_binary_tree, number_1, number_2, number_3, number_4):
    instance_binary_tree.insert(number_1)
    instance_binary_tree.insert(number_2)
    instance_binary_tree.insert(number_3)
    instance_binary_tree.insert(number_4)
    assert instance_binary_tree.left.value == number_1
    assert instance_binary_tree.right.value == number_2
    assert instance_binary_tree.left.left.value == number_3
    assert instance_binary_tree.left.right.value == number_4


@pytest.mark.parametrize("number", [random.randint(1, 1000000) for _ in range(100)])
def test_lookup_binary_tree(instance_binary_tree, number):
    instance_binary_tree.insert(17)
    instance_binary_tree.insert(72)
    instance_binary_tree.insert(12)
    instance_binary_tree.insert(23)
    instance_binary_tree.insert(number)
    assert instance_binary_tree.lookup(number) is not None
    assert instance_binary_tree.lookup(-1) is None


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
    assert instance_graph.lookup_vertex(2).vertex == 2
