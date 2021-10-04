# -*- coding: utf-8 -*-
"""
   Implements simple FileReader
"""


class FileReader:
    """
       Implements simple FileReader
    """

    def __init__(self, filename, mode, encoding):
        self.filename = filename
        self.mode = mode
        self._encoding = encoding
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode, encoding=self._encoding)
        return self.file

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.file.close()


with FileReader('test.txt', 'w', encoding='UTF-8') as f:
    f.write('Test')

print(f.closed)
