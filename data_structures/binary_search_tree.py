# -*- coding: utf-8 -*-
"""
   Implements of simple BinaryTree.
"""


class BinaryTree:
    """
    Implement simple BinaryTree.
    """

    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def insert(self, data):
        """
        Add item.
        """

        if self.value:
            if data < self.value:
                if self.left is None:
                    self.left = BinaryTree(value=data)
                else:
                    self.left.insert(data)

            elif data > self.value:
                if self.right is None:
                    self.right = BinaryTree(value=data)
                else:
                    self.right.insert(data)
        else:
            self.value = data

    def lookup(self, key):
        """
        Find an element by value and return a reference to it (node).
        """
        if self.value == key:
            return self
        if self.left is not None:
            temp = self.left.lookup(key)
            if temp is not None:
                return temp
        if self.right is not None:
            temp = self.right.lookup(key)
            return temp
        return None

    def delete(self, key):
        """
        Remove item by value.
        """

        if self is None:
            return self
        if key < self.value:
            if self.left:
                self.left = self.left.delete(key)
            return self
        if key > self.value:
            if self.right:
                self.right = self.right.delete(key)
            return self
        if self.right is None:
            return self.left
        if self.left is None:
            return self.right
        min_larger_node = self.right
        while min_larger_node.left:
            min_larger_node = min_larger_node.left
        self.value = min_larger_node.value
        self.right = self.right.delete(min_larger_node.value)
        return self

    def display_tree(self):
        """
        Display binary tree.
        """

        if self.left:
            self.left.display_tree()
        print(self.value)
        if self.right:
            self.right.display_tree()


if __name__ == '__main__':
    root = BinaryTree(50)
    root.insert(17)
    root.insert(72)
    root.insert(12)
    root.insert(23)
    print(root.delete(12))
    root.insert(54)
    root.insert(76)
    root.insert(9)
    root.insert(14)
    root.insert(67)
    root.display_tree()
    print('======================================================')
    print(root.lookup(54))
    print(root.delete(17))
    root.display_tree()
