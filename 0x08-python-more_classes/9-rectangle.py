#!/usr/bin/python3
"""Rectangle class: defines a rectangle"""


class Rectangle:
    """Represents a rectangle"""
    print_symbol = "#"
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initializes Rectangle instance attributes
        Args:
        width (int): width of Rectangle once instance is created
        height (int): height of Rectangle once instance is created"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        if not isinstance(self.print_symbol, str):
            self.print_symbol = str(self.print_symbol)
        rectangle = []
        for i in range(self.__height):
            for j in range(self.__width):
                rectangle.append(self.print_symbol)
            if i < (self.__height - 1):
                rectangle.append("\n")
        printRectangle = "".join(rectangle)
        return (printRectangle)

    def __repr__(self):
        """Method to represent Rectangle class object as machine language"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """Method to print when an instance of Rectangle is deleted"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Static method that returns the biggest rectangle based on area
        Args:
        rect_1 (Rectangle): first object to compare
        rect_2 (Rectangle): second object to compare"""
        if type(rect_1) != Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) != Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        rect1Area = rect_1.area()
        rect2Area = rect_2.area()
        if rect1Area >= rect2Area:
            return rect_1
        if rect1Area < rect2Area:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """Method that returns a new Rectangle instance
        Args:
        size (int): width == hewight == size"""
        return cls(size, size)
