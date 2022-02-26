from typing import Union, Sequence


def stairway_path(stairway: Sequence[Union[float, int]]) -> Union[float, int]:
    """
    Calculate min cost of getting to the top of stairway if agent can go on next or through one step.

    :param stairway: list of ints, where each int is a cost of appropriate step
    :return: minimal cost of getting to the top
    """

    #Определяем начальные значения
    previous2_strw = stairway[0]
    previous1_strw = stairway[1]

    for cost in range(2, len(stairway)):
        current_strw = stairway[cost] + min(previous2_strw, previous1_strw)
        previous2_strw, previous1_strw = previous1_strw, current_strw
    return previous1_strw
