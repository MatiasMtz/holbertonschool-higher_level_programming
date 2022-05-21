#!/usr/bin/python3
"""Module that divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """
    Args:
    matrix (list): list of integers or floats
    div (int/float): matrix divider
    """
    if type(matrix) != list:
        raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")

    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    size = None
    for row in matrix:

        if type(row) != list:
            raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")

        if size is None:
            size = len(row)
        elif size != len(row):
            raise TypeError("Each row of the matrix must have the same size")

        for number in row:
            if type(number) != int and type(number) != float:
                raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")

    result = []
    for row in matrix:
        result.append(list(map(lambda x: round(x / div, 2), row)))
    return result
