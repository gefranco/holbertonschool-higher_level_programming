#!/usr/bin/python3
"""
"models" module.

The model module supplies the model classes
"""

from models.base import Base


class Rectangle(Base):

    def __init__(self, width, height, x=0, y=0, id=None):

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")


        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        return self.__height * self.__width

    def display(self):
        for i in range(0, self.__y):
            print()
        for i in range(0, self.__height):
            for j2 in range(0, self.__x):
                    print(" ",end="")
            for j in range(0, self.__width):
                print("#", end="")
            print()

    def __str__(self):
        return "[Rectangle] (" + str(self.id) + ") " + str(self.__x) + "/" + str(self.__y) + " - " + str(self.__width) + "/" + str(self.__height)


    def update(self, *args, **kwargs):
        
        if args is not None and len(args) > 0:

            if len(args) > 0:
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
            if kwargs.get("id") is not None:
                self.id = kwargs.get("id")
            if kwargs.get("width") is not None:
                self.width = kwargs.get("width")
            if kwargs.get("height") is not None:
                self.height = kwargs.get("height")
            if kwargs.get("x") is not None:
                self.x = kwargs.get("x")
            if kwargs.get("y") is not None:
                self.y = kwargs.get("y")

    def to_dictionary(self):
        dictionary = {}
        dictionary["id"] = self.id
        dictionary["width"] = self.width
        dictionary["height"] = self.height
        dictionary["x"] = self.x
        dictionary["y"] = self.y
        return dictionary
