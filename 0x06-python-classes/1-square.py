#!/usr/bin/python3
"""Square class: defines a square"""


class Square:
    """Represents a square"""
    def __init__(self, size):
        """Initializes private square size attribute
        Args:
        size (int): the size of the square once instance is created"""
        self.__size = size
