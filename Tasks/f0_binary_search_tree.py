"""
You can do it either with networkx ('cause tree is a graph)
or with dicts (smth like {'key': 0, value: 123, 'left': {...}, 'right':{...}})
"""

from typing import Any, Optional, Tuple
import networkx as nx


class Node:
    def __init__(self, key: int, value: Any):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

    def make_node(self):
        node_ = {
            "key": self.key,
            "value": self.value,
            "left": self.left,
            "right": self.right
        }
        return node_


class BinarySearchTree:

    def __init__(self):
        self.root = None

    def insert(self, key: int, value: Any) -> None:
        """
        Insert (key, value) pair to binary search tree

        :param key: key from pair (key is used for positioning node in the tree)
        :param value: value associated with key
        :return: None
        """
        if self.root is None:
            self.root = Node(key, value)
        else:
            current_node = self.root
            current_key = Node(key, value)

    def remove(self, key: int) -> Optional[Tuple[int, Any]]:
        """
        Remove key and associated value from the BST if exists

        :param key: key to be removed
        :return: deleted (key, value) pair or None
        """
        print(key)
        return None

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
        self.root = None
