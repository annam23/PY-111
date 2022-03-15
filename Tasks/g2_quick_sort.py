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
    left = []
    right = []
    pivot_cont = []

    for value in container:
        if value < pivot:
            left.append(value)
        elif value > pivot:
            right.append(value)
        else:
            pivot_cont.append(value)

    return sort(left) + pivot_cont + sort(right)
