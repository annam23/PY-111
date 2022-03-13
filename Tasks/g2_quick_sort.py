from typing import List
from random import choice


def sort(container: List[int]) -> List[int]:
    """
    Sort input container with quick sort

    :param container: container of elements to be sorted
    :return: container sorted in ascending order
    """
    if not container:
        return []

    pivot = choice(container)
    left = [value for value in container if value < pivot]
    pivot_v = [value for value in container if value == pivot]
    right = [value for value in container if value > pivot]

    return sort(left) + pivot_v + sort(right)
