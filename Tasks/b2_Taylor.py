"""
Taylor series
"""
from typing import Union
TOCHNOST = 100


def ex(x: Union[int, float]) -> float:
    """
    Calculate value of e^x with Taylor series

    :param x: x value
    :return: e^x value
    """

    value, res, factorial = 1, 1, 1

    for elem in range(1, TOCHNOST):
        factorial *= elem
        value *= x
        res += value / factorial
    return res


def sinx(x: Union[int, float]) -> float:
    """
    Calculate sin(x) with Taylor series

    :param x: x value
    :return: sin(x) value
    """
    value, res = x, x
    fact = 1
    for elem in range(1, TOCHNOST):
        fact *= (2 * elem + 1)
        value *= (-1) ** elem * x ** 2
        res += value / fact

    return res

