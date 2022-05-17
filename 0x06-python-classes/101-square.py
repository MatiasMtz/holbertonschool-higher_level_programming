#!/usr/bin/python3
"""Square class: defines a square"""


class Square:
    """Represents a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes private square size attribute and position attribute
        Args:
        size (int): the size of the square once instance is created
        position (int): position where the square is going to be placed"""

        self.__size = size
        self.position = position

    def area(self):
        """Initializes public square area attribute"""

        return (self.__size * self.__size)

    @property
    def size(self):
        """Initializes square size return"""
        return (self.__size)

    @property
    def position(self):
        """Initializes square position"""
        return (self.__position)

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

    @position.setter
    def position(self, value):
        """Initializes square position attribute
        Args:
        value (int): the position of the square"""

        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def my_print(self):
        """Initializes square printing"""

        if self.__size == 0:
            print()
            return
        else:
            for position1 in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for position2 in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print()

    def __str__(self):
        square = []
        if self.__size == 0:
            return ''
        for newlines in range(self.__position[1]):
            square.append('\n')
        for rows in range(self.__size):
            for spaces in range(self.__position[0]):
                square.append(' ')
            for hashes in range(self.__size):
                square.append('#')
            if rows != self.__size - 1:
                square.append('\n')
        return ''.join(square)
