#!/usr/bin/python3
"""Rectangle class: defines a rectangle"""


class Rectangle:
    """Represents a rectangle"""

    def __init__(self, width=0, height=0):
        """Initializes Rectangle attributes
        Args:
        width (int): width of Rectangle once instance is created
        height (int): height of Rectangle once instance is created"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Defines a private instance: Width"""
        return (self.__width)

    @property
    def height(self):
        """Defines a private instance: Height"""
        return (self.__height)

    @width.setter
    def width(self, value):
        """Rectangle width attribute setter
        Args:
        value (int): Width of the Rectangle"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """Rectangle height attribute setter
        Args:
        value (int): Height of the Rectangle"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Public instance method that returns the Rectangle area"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Public instance method that returns the Rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        else:
            return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """Method to represent Rectangle class object as a string"""
        if self.width == 0 or self.__height == 0:
            return ""
        rectangle = []
        for i in range(self.__height):
            for j in range(self.__width):
                rectangle.append("#")
            if i < (self.__height - 1):
                rectangle.append("\n")
        printRectangle = "".join(rectangle)
        return (printRectangle)

    def __repr__(self):
        """Method to represent Rectangle class object as machine language"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)
