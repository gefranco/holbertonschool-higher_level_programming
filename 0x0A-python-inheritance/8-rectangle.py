#!/usr/bin/python3
"""
"8-rectangle" module.

The 8-rectangle supplies the class Rectangle
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    class BaseGeometry
    """

    def __init__(self, width, height):
            self.integer_validator("width", width)
            self.__width = width
            self.integer_validator("height", height)
            self.__height = height
