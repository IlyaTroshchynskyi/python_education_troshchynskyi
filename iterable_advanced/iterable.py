# -*- coding: utf-8 -*-
"""calc
   Implements iterable class Sentence with wrapper
"""

import re
from typing import Union, Callable


class MultipleSentencesError(Exception):
    """
    Custom exception. It is used when user put multiple sentences instead one.
    """
    def __init__(self, *args):
        self.message = "You pass multiple sentences"
        super().__init__(*args)


class Sentence:
    """
    Implements class Sentence which has behavior like iterator.
    """
    def __init__(self, text: str):
        if not isinstance(text, str):
            raise TypeError("You should pass the string")

        if not Sentence.check_multiple_sentences(text):
            raise MultipleSentencesError

        if not Sentence.check_full_sentences(text):
            raise ValueError("You should pass full sentence")

        self.text = Sentence.replace_extra_spaces(text)
        self.indexes = Sentence.define_indexes_of_spaces(self.text)
        self.indexes.append(len(self.clear_signs(self.text)))

    @staticmethod
    def check_multiple_sentences(text: str) -> bool:
        """
        Checks if the text contains multiple sentences.
        """
        search_sentence = re.compile(r'^[A-Za-z0-9,:"\- ]+(\.\.\.|\.|\?|!)$')
        if re.fullmatch(search_sentence, text):
            return True
        return False

    @staticmethod
    def check_full_sentences(text: str) -> bool:
        """
        Checks if the text is a complete sentence.
        """
        for sign in ('...', '.', '!', '?'):
            if text.endswith(sign):
                return True
        return False

    @staticmethod
    def clear_signs(text: str) -> str:
        """
        Removes punctuation characters from text
        """
        new_word = ''
        for sign in list(text):
            if sign not in (".", "!", "?", "'"):
                new_word += sign
        return new_word.replace(' -', '')

    @staticmethod
    def replace_extra_spaces(text: str) -> str:
        """
        Replace extra spaces from the text.
        """
        count = 0
        count_spaces = set()
        for sign in text:
            if sign == ' ':
                count += 1
            else:
                count_spaces.add(count)
                count = 0
        count_spaces.discard(1)
        for number_spaces in sorted(list(count_spaces), reverse=True):
            if number_spaces >= 2:
                text = text.replace(" " * number_spaces, " ")
        return text

    @staticmethod
    def define_indexes_of_spaces(text: str) -> list:
        """
        Define indexes of spaces for slicing.
        """
        indexes = [0]
        for index, sign in enumerate(Sentence.clear_signs(text)):
            if sign == ' ':
                indexes.append(index)
        return indexes

    def __getitem__(self, index: Union[int, slice]):
        if isinstance(index, slice):
            start, stop, step = index.indices(len(self.text))
            if start == 0 and stop == 0:
                return ''.join([self.clear_signs(self.text)[i]
                                for i in range(start, stop, step)]).strip()
            if start < 0 or stop < 0:
                raise IndexError("Index must be positive")
            return self.clear_signs(self.text)[self.indexes[start]:self.indexes[stop]].strip()
        if index < 0:
            raise IndexError("Index must be positive")
        if isinstance(index, int):
            return self.clear_signs(self.text)[self.indexes[index]:self.indexes[(index+1)]].strip()
        raise TypeError('Invalid argument type: {}'.format(type(index)))

    def __repr__(self):
        return f"<Sentence(words={self.get_count_words}, other_chars={self.get_count_chars})>"

    def __iter__(self):
        return SentenceIterator(self.text, self.indexes, self.clear_signs)

    def _words(self):
        for word in self.text.split(" "):
            yield word

    @property
    def get_count_words(self) -> int:
        """
        Get count words
        """
        return len(self.text.split(" "))

    @property
    def get_count_chars(self) -> int:
        """
        Get count chars
        """
        return len(self.other_chars)

    @property
    def words(self) -> list:
        """
        Returns a list of all words in a sentence.
        """
        return list(self._words())

    @property
    def other_chars(self) -> list:
        """
        Returns a list of all non-words in a sentence.
        """
        signs = []
        for sign in list(self.text):
            if sign in (".", "!", "?", ",", "-"):
                signs.append(sign)
        return signs


class SentenceIterator:
    """
    Implementation of iterator
    """
    def __init__(self, text: str, indexes: list, clear_signs: Callable):
        self.text = text
        self.index = 0
        self.indexes = indexes
        self.clear_signs = clear_signs

    def __len__(self):
        return len(self.text.split(" "))

    def __next__(self):
        if self.index >= len(self):
            raise StopIteration()
        result = self.clear_signs(self.text)[self.indexes[self.index]:self.indexes[self.index+1]]
        self.index += 1
        return result.strip()

    def __iter__(self):
        return self


sentence = Sentence("We implement new - version of iterator!")
print(sentence)
print(sentence[2:4])
# print(sentence._words())
# print(next(sentence._words()))
print(sentence.other_chars)

for item in Sentence('Hello world!'):
    print(item)

print(iter(sentence))
iterator_1 = iter(sentence)
print(next(iterator_1))
print(next(iterator_1))
