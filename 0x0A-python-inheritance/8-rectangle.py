#!/usr/bin/python3
"""Rectangle class"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Inherits from BaseGeometry"""
    def __init__(self, width, height):
        """Instantiation of Rectangle width and height
        Args:
        width (int), height (int): size of the rectangle"""
        super().__init__()
        super().integer_validator("height", height)
        super().integer_validator("width", width)
        self.__width = width
        self.__height = height
