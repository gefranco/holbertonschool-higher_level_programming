#!/usr/bin/python3
"""
"11-rectangle" module.

The 11-rectangle supplies the class Rectangle
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    class Square, inherits from Rectangle
    """

    def __init__(self, size):
            Rectangle.__init__(self, size, size)
            self.__size = size

    def __str__(self):

        return "[Square] " + str(self.__size) + "/" + str(self.__size)
