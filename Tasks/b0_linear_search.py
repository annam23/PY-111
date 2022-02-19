"""
This module implements some functions based on linear search algo
"""
from typing import Sequence


def min_search(arr: Sequence) -> int:
    """
    Function that find minimal element in array

    :param arr: Array containing numbers
    :return: index of first occurrence of minimal element in array
    """
    min_val = arr[0]
    index_of_min_val = 0

    for index, current_value in enumerate(arr):
        if current_value < min_val:
            min_val = current_value
            index_of_min_val = index
    return index_of_min_val
