def fib_recursive(n: int) -> int:
    """
    Calculate n-th number of Fibonacci sequence using recursive algorithm

    :param n: number of item
    :return: Fibonacci number
    """
    if n < 0:
        raise ValueError
    elif n in (0, 1):
        return n
    else:
        return fib_recursive(n - 1) + fib_recursive(n - 2)


def fib_iterative(n: int) -> int:
    """
    Calculate n-th number of Fibonacci sequence using iterative algorithm

    :param n: number of item
    :return: Fibonacci number
    """
    f1 = 0 #Первое число Фибоначчи
    f2 = 1 #Второе число Фибоначчи

    if n < 0:
        raise ValueError
    if n in (0, 1):
        return n

    for _ in range(n - 2):
        f1, f2 = f2, f2 + f1
    return f2




