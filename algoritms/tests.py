# -*- coding: utf-8 -*-
"""
   Collect all tests for algorithms
"""

import random
import math
import pytest


from algoritms import factorial, binary_search, quick_sort


@pytest.mark.parametrize("number", list(range(100)))
def test_factorial(number):
    """
    Test recursive func for definition factorial.
    """
    assert factorial(number) == math.factorial(number)


@pytest.mark.parametrize("number", [random.randint(0, 10000) for _ in range(1000)])
def test_binary_search(number):
    """
    Test func binary search which return index of element.
    """
    test_list = list(range(10000))
    assert binary_search(test_list, number) == test_list.index(number)


@pytest.mark.parametrize("array", [[random.randint(0, 50) for _ in range(20)] for x in range(50)])
def test_quick_sort(array):
    """
    Test quick sort of arrays iterative method.
    """
    test_array = array[:]
    quick_sort(array, 0, len(array) - 1)
    assert array == sorted(test_array)
