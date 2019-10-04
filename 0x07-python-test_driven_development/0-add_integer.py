#!/usr/bin/python3
"""
"0-add_integer" module.

The 0-add_integer module supplies the function add_integer
"""


def add_integer(a, b=98):
    """
    Return the sum of 2 integers.
    """
    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    if type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")

    return int(a) + int(b)
