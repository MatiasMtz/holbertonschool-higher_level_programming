#!/usr/bin/python3
""""""
from models.base import Base

class Rectangle(Base):
    """"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """"""
        return self.__width

    @width.setter
    def width(self, value):
        """"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        else:
            if value <= 0:
                raise ValueError("width must be > 0")
            else:
                self.__width = value

    @property
    def height(self):
        """"""
        return self.__height

    @height.setter
    def height(self, value):
        """"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        else:
            if value <= 0:
                raise ValueError("height must be > 0")
            else:
                self.__height = value

    @property
    def x(self):
        """"""
        return self.__x

    @x.setter
    def x(self, value):
        """"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        else:
            if value < 0:
                raise ValueError("x must be >= 0")
            else:
                self.__x = value

    @property
    def y(self):
        """"""
        return self.__y

    @y.setter
    def y(self, value):
        """"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        else:
            if value < 0:
                raise ValueError("y must be >= 0")
            else:
                self.__y = value

    def area(self):
        """"""
        return self.width * self.height

    def display(self):
        """"""
        for ejey in range(self.y):
            print()
        for columns in range(self.height):
            for ejex in range(self.x):
                print(" ", end="")
            for rows in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        """"""
        i = self.id
        x = self.x
        y = self.y
        w = self.width
        h = self.height
        return f"[Rectangle] ({i}) {x}/{y} - {w}/{h}"

    def update(self, *args, **kwargs):
        """"""
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
        """"""
        dcty = {'id': self.id, 'width': self.width, 'height': self.height,
                      'x': self.x, 'y': self.y}
        return dcty
