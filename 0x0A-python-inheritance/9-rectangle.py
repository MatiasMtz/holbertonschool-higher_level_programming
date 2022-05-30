#!/usr/bin/python3
"""BaseGeometry class"""


class BaseGeometry:
    """raises exceptions"""
    def area(self):
        """raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """value validator"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


"""Rectangle class"""


class Rectangle(BaseGeometry):
    """Inherits from BaseGeometry"""
    def __init__(self, width, height):
        """Instantiation of Rectangle width and height
        Args:
        width (int), height (int): size of the rectangle"""
        BaseGeometry.integer_validator(self, "height", height)
        BaseGeometry.integer_validator(self, "width", width)
        self.__width = width
        self.__height = height

    def area(self):
        """calculates Rectangle area"""
        return self.__width * self.__height

    def __str__(self):
        """returns Rectangle description"""
        return f"[Rectangle] {self.__width}/{self.__height}"
