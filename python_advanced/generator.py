# -*- coding: utf-8 -*-
"""
   Implements simple string generator
"""


class StringGenerator:
    """
    Implement simple string generator
    """

    def __init__(self, text):
        self.text = text
        self.iter_text = iter(text)
        self.length = len(text)

    def __iter__(self):
        return self

    def __next__(self):
        if self.length == 0:
            raise StopIteration
        next_obj = next(self.iter_text)
        self.length -= 1
        return next_obj


string_generator = StringGenerator("abc")
print(string_generator)
print(next(string_generator))

string_generator = StringGenerator("abc")

for letter in string_generator:
    print(letter)
