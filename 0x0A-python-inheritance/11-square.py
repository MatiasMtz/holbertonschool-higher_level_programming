#!/usr/bin/python3
"""Square class"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Inherits from Rectangle"""
    def __init__(self, size):
        """Instantiation of Square size
        Args:
        size (int): size of the Square"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """calculates Square area"""
        return self.__size * self.__size

    def __str__(self):
        """Prints description of Square size"""
        return f"[Square] {self.__size}/{self.__size}"
