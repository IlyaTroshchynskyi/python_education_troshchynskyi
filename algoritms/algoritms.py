# -*- coding: utf-8 -*-
"""calc
   Implements algorithms:
    - Binary search
    - Quick sort (iterative)
    - Recursive factorial
"""


def factorial(number):
    """
    Define factorial certain number.
    """
    if number <= 0:
        return 1
    return number * factorial(number-1)


print(factorial(50))


test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]


def binary_search(input_list, number):
    """
    Look for index of certain number by using algorithms binary search.
    Return None if number out of list.
    """
    start = 0
    stop = len(input_list) - 1
    while start <= stop:
        middle = (stop + start) // 2
        guess = input_list[middle]
        if guess == number:
            return middle
        if guess > number:
            stop = middle - 1
        else:
            start = middle + 1
    return None


print(binary_search(test_list, 10))


def partition(my_list, start_index, end_index):
    """
    Elements less than the last will go to the left of array and
    elements more than the last will go to the right of array
    """
    start_index_1 = (start_index - 1)
    last_element = my_list[end_index]

    for j in range(start_index, end_index):
        if my_list[j] <= last_element:

            start_index_1 = start_index_1 + 1
            my_list[start_index_1], my_list[j] = my_list[j], my_list[start_index_1]

    my_list[start_index_1 + 1], my_list[end_index] = my_list[end_index], my_list[start_index_1 + 1]
    return start_index_1 + 1


def quick_sort(my_list, start_index, end_index):
    """
    Sort array in ascending order by using algorithms quick sort.
    """

    size = end_index - start_index + 1
    stack = [0] * size
    top = -1

    top = top + 1
    stack[top] = start_index
    top = top + 1
    stack[top] = end_index

    while top >= 0:

        end_index = stack[top]
        top = top - 1
        start_index = stack[top]
        top = top - 1

        res_partition = partition(my_list, start_index, end_index)

        if res_partition - 1 > start_index:
            top = top + 1
            stack[top] = start_index
            top = top + 1
            stack[top] = res_partition - 1

        if res_partition + 1 < end_index:
            top = top + 1
            stack[top] = res_partition + 1
            top = top + 1
            stack[top] = end_index


test_list = [4, 3, 5, 2, 1, 3, 2, 3]
quick_sort(test_list, 0, len(test_list) - 1)
for i, value in enumerate(test_list):
    print(f"Index: {i} Element:{value}")
