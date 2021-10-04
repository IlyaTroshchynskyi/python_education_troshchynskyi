# -*- coding: utf-8 -*-
"""
   Implements simple iterator
"""


class MyIterator:
    """
       Implements simple iterator
    """

    def __init__(self, value):
        self.data = value
        self.index = 0

    def __getitem__(self, index):
        return self.data[index]

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == len(self.data):
            raise StopIteration
        item = self.data[self.index]
        self.index += 1
        return item

    def __contains__(self, item):
        return item in self.data


my_iterator = MyIterator([1, 2, 3, 4, 5])
print(3 in my_iterator)
for element in my_iterator:
    print(element)
