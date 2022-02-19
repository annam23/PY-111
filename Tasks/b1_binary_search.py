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

    #Условие, пока возможен поиск
    while start_index <= end_index:

    #Определяем, как делить последовательность
        middle_index = (start_index + end_index) // 2
        middle_elem = arr[middle_index]

    #Рассматриваем сценарии поиска:
        if middle_elem == elem:
            return middle_elem
        elif middle_elem > elem:
            end_index = middle_index
        elif middle_elem < elem:
            start_index = middle_index




