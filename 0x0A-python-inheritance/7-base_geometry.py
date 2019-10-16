#!/usr/bin/python3
"""
"7-base_geometry" module.

The 7-base_geometry supplies the class BaseGeometry
"""


class BaseGeometry:
    """
    class BaseGeometry
    """
    def area(self):
        """
        unimplemented method
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Function that validates value
        """
        if type(value) is not int:
            raise TypeError(name + " must be an integer")
        elif value <= 0:
            raise ValueError(name + " must be greater than 0")
