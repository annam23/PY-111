from typing import Sequence, Optional


def binary_search(elem: int, arr: Sequence, start_index=0, end_index=None) -> Optional[int]:
    """
    Performs binary search of given element inside of array (using recursive way)

    :param elem: element to be found
    :param arr: array where element is to be found
    :param start_index: where we start to search
    :param end_index: where we end to search
    :return: Index of element if it's presented in the arr, None otherwise
    """
    if end_index is None:
        end_index = len(arr) - 1

    while start_index < end_index:
        middle_index = (start_index + end_index) // 2
        if arr[middle_index] < elem:
            return binary_search(elem, arr, middle_index + 1, end_index)
        else:
            return binary_search(elem, arr, start_index, middle_index)

    return start_index if arr[start_index] == elem else None

