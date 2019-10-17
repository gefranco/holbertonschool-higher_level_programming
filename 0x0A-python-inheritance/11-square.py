#!/usr/bin/python3
"""
"10-rectangle" module.

The 10-rectangle supplies the class Rectangle
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    class Square, inherit from Rectangle
    """

    def __init__(self, size):
        super().integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        return "[Square] " + str(self.__width) + "/" + str(self.__height)
