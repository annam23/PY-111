"""
You can do it either with networkx ('cause tree is a graph)
or with dicts (smth like {'key': 0, value: 123, 'left': {...}, 'right':{...}})
"""
from functools import total_ordering
from typing import Any, Optional, Tuple
import networkx as nx


@total_ordering
class Node:
    def __init__(self, key: int, value: Any):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

    @staticmethod
    def is_valid_node(value):
        if not isinstance(value, (Node, type(None))):
            raise ValueError
        return True

    @property
    def left(self) -> Optional["Node"]:
        return self._left

    @property
    def right(self) -> Optional["Node"]:
        return self._right

    @left.setter
    def left(self, value):
        if self.is_valid_node(value):
            self._left = value

    @right.setter
    def right(self, value):
        if self.is_valid_node(value):
            self._right = value

    def __str__(self):
        if self.is_list():
            return f"{self.key}"
        return f"{self.key}: (Left: {self.left} Right: {self.right})"

    # Для сравнения Нод между собой
    def __eq__(self, other):
        if isinstance(other, int):
            return self.key == other
        elif isinstance(other, (Node, int)):
            return self.key == other.key

        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, int):
            return self.key < other
        elif isinstance(other, (Node, int)):
            return self.key < other.key

        return NotImplemented

    def is_list(self) -> bool:
        return self.left is self.right is None


class BinarySearchTree:

    def __init__(self):
        self._root = None

    def insert(self, key: int, value: Any) -> None:
        """
        Insert (key, value) pair to binary search tree

        :param key: key from pair (key is used for positioning node in the tree)
        :param value: value associated with key
        :return: None
        """
        current_node, prev_node = self._find(key)
        if current_node is not None:
            current_node.value = value
            return

        new_node = Node(key, value)
        if prev_node is None:
            self._root = new_node
        elif new_node < prev_node:
            prev_node.left = new_node
        else:
            prev_node.right = new_node

    def remove(self, key: int) -> Optional[Tuple[int, Any]]:
        """
        Remove key and associated value from the BST if exists

        :param key: key to be removed
        :return: deleted (key, value) pair or None
        """
        current_node, prev_node = self._find(key)
        if current_node is None:
            return

        del_node = current_node
        del_ = (del_node.key, del_node.value)

        if prev_node is None:
            self._root = None
            return del_

        if current_node is None:
            raise KeyError

        #  Если удаляем лист
        if current_node.is_list():
            if prev_node.right == current_node:
                prev_node.right = None
                return del_
            else:
                prev_node.left = None
                return del_

        # Если у поддерева нет одного из детей, удаляем узел и заменяем потомком
        elif current_node.right is None or current_node.left is None:
            if prev_node.right == current_node:
                prev_node.right = current_node.right
                return del_
            if prev_node.right == current_node:
                prev_node.right = current_node.left
                return del_
            if prev_node.left == current_node:
                prev_node.left = current_node.left
                return del_
            if prev_node.left == current_node:
                prev_node.left = current_node.right
                return del_

        # Оба поддерева есть
        else:
            # Удаление текущего узла
            del_node = current_node
            new_current_node = current_node.right

            # Поиск минимального потомка
            while True:
                if new_current_node.left is None:
                    break
                new_current_node = new_current_node.left

            # Переприсвоение текущему узлу минимального найденного
            current_node = new_current_node
            return del_


    def find(self, key: int) -> Optional[Any]:
        """
        Find value by given key in the BST

        :param key: key for search in the BST
        :return: value associated with the corresponding key
        """
        current_node, _ = self._find(key)
        if current_node is not None:
            return current_node.value

        if current_node is None:
            raise KeyError

    def _find(self, key) -> Tuple[Optional[Node], Optional[Node]]:
        current_node, prev_node = self._root, None
        while current_node is not None:
            if current_node == key:
                break

            prev_node = current_node
            if current_node < key:
                current_node = current_node.right
            else:
                current_node = current_node.left

        return current_node, prev_node

    def clear(self) -> None:
        """
        Clear the tree

        :return: None
        """
        self._root = None
        return None

