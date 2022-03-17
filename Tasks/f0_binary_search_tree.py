"""
You can do it either with networkx ('cause tree is a graph)
or with dicts (smth like {'key': 0, value: 123, 'left': {...}, 'right':{...}})
"""

from typing import Any, Optional, Tuple
import networkx as nx


class BinarySearchTree:
    class Node:
        def __init__(self, key: int, value: Any):
            self.key = key
            self.value = value
            self.left = None
            self.right = None


        @property
        def left(self) -> Optional["Node"]:
            return self.left

        @staticmethod
        def is_valid_node(value):
            if not isinstance(value, (Node, type(None))):
                raise ValueError
            return True
        @property
        def right(self) -> Optional["Node"]:
            return self.right

        @left.setter
        def left(self, value):
            if self.is_valid_node(value):
                self._left = value

        @right.setter
        def right(self, value):
            if self.is_valid_node(value):
                self._right = value

        def __str__(self):
            return f"{self.key}: (Left: {self.left} Right: {self.right})"

    def __init__(self):
        self.root = None

    def insert(self, key: int, value: Any) -> None:
        """
        Insert (key, value) pair to binary search tree

        :param key: key from pair (key is used for positioning node in the tree)
        :param value: value associated with key
        :return: None
        """
        new_node = self.Node(key, value)

        #Определяем, есть ли корень и создаем его
        if self.root is None:
            self.root = new_node
        else:
            current_node = self.root
            while True:
                if new_node > current_node:
                    if current_node.right is None:
                        current_node.right = new_node
                        break
                    current_node = current_node.right()

                elif new_node < current_node:
                    if current_node.left is None:
                        current_node.left = new_node
                        break
                    current_node = current_node.left()

                else:
                    current_node.value = value
                    break

    def remove(self, key: int) -> Optional[Tuple[int, Any]]:
        """
        Remove key and associated value from the BST if exists

        :param key: key to be removed
        :return: deleted (key, value) pair or None
        """
        if self.root is None:
            return None
        else:
            current_node = self.root
            while True:


    def find(self, key: int) -> Optional[Any]:
        """
        Find value by given key in the BST

        :param key: key for search in the BST
        :return: value associated with the corresponding key
        """
        print(key)
        return None

    def clear(self) -> None:
        """
        Clear the tree

        :return: None
        """
        self.root.clear()
