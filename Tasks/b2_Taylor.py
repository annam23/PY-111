"""
Taylor series
"""
from typing import Union
TOCHNOST_N = 100

def ex(x: Union[int, float]) -> float:
    """
    Calculate value of e^x with Taylor series

    :param x: x value
    :return: e^x value
    """
    res = 1
    factorial = 1

    for elem in range(1, TOCHNOST_N):
        factorial *= elem
        res += (x ** elem) / factorial

    return res


def sinx(x: Union[int, float]) -> float:
    """
    Calculate sin(x) with Taylor series

    :param x: x value
    :return: sin(x) value
    """
    res = x
    fact = 1
    for elem in range(1, 10):
        fact *= (2 * elem + 1)
        res += ((-1) ** elem) * (x ** (2 * elem + 1)) / fact
        print(fact, res)

    return res

ex(6)
sinx(5)