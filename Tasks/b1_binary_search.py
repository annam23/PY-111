from typing import Sequence, Optional


def binary_search(elem: int, arr: Sequence) -> Optional[int]:
    """
    Performs binary search of given element inside of array

    :param elem: element to be found
    :param arr: array where element is to be found
    :return: Index of element if it's presented in the arr, None otherwise
    """
    #Определяем границы поиска
    start_index = 0
    end_index = len(arr) - 1

    #Условие, пока возможен поиск и при повторах возьмем 1 вхождение элемента
    while start_index < end_index:

    # Определяем, как делить последовательность
        middle_index = (start_index + end_index) // 2
        if arr[middle_index] < elem:
            start_index = middle_index +1
        else:
            end_index_index = middle_index

    return start_index if arr[start_index] == elem else None







