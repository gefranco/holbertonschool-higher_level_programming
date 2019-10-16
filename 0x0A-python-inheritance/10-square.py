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
            Rectangle.__init__(self, size, size)
