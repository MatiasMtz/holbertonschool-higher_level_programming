#!/usr/bin/python3
"""Rectangle class: defines a rectangle"""


class Rectangle:
    """Represents a rectangle"""

    def __init__(self, width=0, height=0):
        """Initializes Rectangle attributes
        Args:
        width (int): width of Rectangle once instance is created
        height (int): height of Rectangle once instance is created"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Defines a private instance: Width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Rectangle width attribute setter
        Args:
        value (int): Width of the Rectangle"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Defines a private instance: Height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Rectangle height attribute setter
        Args:
        value (int): Height of the Rectangle"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
