"""
Priority Queue

Queue priorities are from 0 to 10
"""
from typing import Any
from collections import defaultdict


class PriorityQueue:
    def __init__(self):
        self._queue_priority = defaultdict(list)

    def enqueue(self, elem: Any, priority: int = 0) -> None:
        """
        Operation that add element to the end of the queue

        :param elem: element to be added
        :return: Nothing
        """
        self._queue_priority[priority].append(elem)

    def dequeue(self) -> Any:
        """
        Return element from the beginning of the queue. Should return None if not elements.

        :return: dequeued element
        """
        for priority in sorted(self._queue_priority.keys()):
            if self._queue_priority:
                return self._queue_priority[priority].pop(0)

    def peek(self, ind: int = 0, priority: int = 0) -> Any:
        """
        Allow you to see at the element in the queue without dequeuing it

        :param ind: index of element (count from the beginning)
        :return: peeked element
        """
        if len(self._queue_priority[priority]) > ind:
            return self._queue_priority[priority][ind]

    def clear(self) -> None:
        """
        Clear my queue

        :return: None
        """
        for priority in self._queue_priority:
            self._queue_priority[priority].clear()
