#!/usr/bin/python3
"""Defines a Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """Class that inherits from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Instantiation of attributes:
        Args:
        width (int): Rectangle width
        height (int): Rectangle height
        x (int): Rectangle x coordinate
        y (int): Rectangle y coordinate
        id (int): Rectangle identification"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Rectangle width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """Rectangle width setter"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        else:
            if value <= 0:
                raise ValueError("width must be > 0")
            else:
                self.__width = value

    @property
    def height(self):
        """Rectangle height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """Rectangle height setter"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        else:
            if value <= 0:
                raise ValueError("height must be > 0")
            else:
                self.__height = value

    @property
    def x(self):
        """Rectangle x coordinate getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """Rectangle x coordinate setter"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        else:
            if value < 0:
                raise ValueError("x must be >= 0")
            else:
                self.__x = value

    @property
    def y(self):
        """Rectangle y coordinate getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """Rectangle y coordinate setter"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        else:
            if value < 0:
                raise ValueError("y must be >= 0")
            else:
                self.__y = value

    def area(self):
        """Function that returns the area value of the Rectangle instance."""
        return self.width * self.height

    def display(self):
        """Function that prints in stdout the Rectangle instance with the
        character #, handling x and y coordinates"""
        for ejey in range(self.y):
            print()
        for columns in range(self.height):
            for ejex in range(self.x):
                print(" ", end="")
            for rows in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        """str overriding to get some Rectangle class information"""
        i = self.id
        x = self.x
        y = self.y
        w = self.width
        h = self.height
        return f"[Rectangle] ({i}) {x}/{y} - {w}/{h}"

    def update(self, *args, **kwargs):
        """Function that assigns an argument or a key/value argument to
        attributes
        Args:
        *args: non-keyworded arguments
        **kwargs: key-worded arguments"""
        if args is not None and len(args) != 0:
            self.id = args[0]
            if len(args) > 1:
                self.width = args[1]
            if len(args) > 2:
                self.height = args[2]
            if len(args) > 3:
                self.x = args[3]
            if len(args) > 4:
                self.y = args[4]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "width":
                    self.width = value
                if key == "height":
                    self.height = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """Function that returns the dict representation of Rectangle"""
        dcty = {'id': self.id, 'width': self.width, 'height': self.height,
                'x': self.x, 'y': self.y}
        return dcty
