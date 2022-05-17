#!/usr/bin/python3
"""Square class: defines a square"""


class Square:
    """Represents a square"""
    def __init__(self, size=0):
        """Initializes private square size attribute
        Args:
        size (int): the size of the square once instance is created"""

        if type(size) != int:
            raise TypeError("size must be an integer")
        else:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
