#!/usr/bin/python3
"""Module that sums two integers"""


def add_integer(a, b=98):
    """
    Args:
    a (int or float): parameter 1
    b (int or float): parameter 2
    """
    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    elif type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")
    else:
        number = int(a)
        number2 = int(b)
        result = number + number2
        return result
