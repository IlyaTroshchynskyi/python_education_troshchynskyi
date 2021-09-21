def is_sorted(array, order_by):
    """
    Determines if the array is sorted or not

    :param array: List of values
    :param order_by: Keyword is used to sort the result-set in ascending or descending order
    :return: bool
    Raises: AttributeError: if order_by not in (ASC, DESC)
    """

    if order_by.upper() == 'ASC':
        return sorted(array) == array
    elif order_by.upper() == 'DESC':
        return sorted(array, reverse=True) == array
    else:
        raise AttributeError


print(is_sorted([1, 2, 3, 4, 5, 6], 'ASC'))
print(is_sorted([7, 4, 5, 4, 2, 1], 'DESC'))
print(is_sorted([1, 2, 3, 6, 5, 6], 'DESC'))
print(is_sorted([1, 2, 3, 7, 5, 6], 'ASC'))
print(is_sorted([7, 4, 3, 2], 'DESC'))