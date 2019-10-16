#!/usr/bin/python3
"""
"9-rectangle" module.

The 9-rectangle supplies the class Rectangle
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    class Rectangle. Inherit from BaseGeometry
    """

    def __init__(self, width, height):
            self.integer_validator("width", width)
            self.__width = width
            self.integer_validator("height", height)
            self. __height = height

    def area(self):
        """
        return self.__width * self.__height
        """
        return (self.__width * self.__height)

    def __str__(self):
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
