#!/usr/bin/python3
class Rectangle:

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.height == 0:
            return 0

        return self.__width * 2 + self.__height * 2

    def __str__(self):
        rep = []

        for j in range(self.__height):
            for i in range(self.__width):
                rep += "#"
            rep += "\n"
        if len(rep) > 0:
            rep.pop()

        return "".join(rep)

    def __repr__(self):
        return "Rectangle(" + str(self.__width) + ", " + str(self.height) + ")"
