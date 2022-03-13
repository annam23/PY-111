from typing import List

def sort(container: List[int]) -> List[int]:
    """
    Sort input container with merge sort

    :param container: container of elements to be sorted
    :return: container sorted in ascending order
    """
    result_container = []

    if len(container) < 2:
        return container

    middle_ind = len(container) // 2
    right, left = sort(container[middle_ind:]), sort(container[:middle_ind])

    index_left = 0
    index_right = 0

    while index_left < len(left) and index_right < len(right):
        if left[index_left] < right[index_right]:
            result_container.append(left[index_left])
            index_left += 1
        else:
            result_container.append(right[index_right])
            index_right += 1

    result_container.extend(right[index_right:])
    result_container.extend(left[index_left:])

    return result_container
