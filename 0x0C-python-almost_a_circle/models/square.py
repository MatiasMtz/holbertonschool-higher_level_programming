#!/usr/bin/python3
""""""
from models.rectangle import Rectangle


class Square(Rectangle):
    """"""
    def __init__(self, size, x=0, y=0, id=None):
        """"""
        self.size = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    @property
    def size(self):
        """"""
        return self.__width

    @size.setter
    def size(self, value):
        """"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width mus be > 0")
        self.__width = value
        self.__height = value

    def update(self, *args, **kwargs):
        """"""
        if args is not None and len(args) != 0:
            self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """"""
        dcty = {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
        return dcty
