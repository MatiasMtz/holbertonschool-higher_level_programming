#!/usr/bin/python3
"""Square class: defines a square"""


class Square:
    """Represents a square"""

    def __init__(self, size=0):
        """Initializes private square size attribute
        Args:
        size (int): the size of the square once instance is created"""

        self.__size = size

    def area(self):
        """Initializes public square area attribute"""

        return (self.__size * self.__size)

    @property
    def size(self):
        """Initializes square size return"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Initializes square size attribute
        Args:
        value (int): the size of a size of the square"""

        if type(value) != int:
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value

    def my_print(self):
        """Initializes square printing"""

        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()
