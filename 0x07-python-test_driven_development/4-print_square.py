#!/usr/bin/python3
"""Module that prints a square"""


def print_square(size):
    """
    Args:
    size (int): large of the square that will be printed
    """
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for height in range(size):
        for width in range(size):
            print("#", end="")
        print()
