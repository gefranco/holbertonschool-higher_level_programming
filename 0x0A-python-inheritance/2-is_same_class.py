#!/usr/bin/python3
"""
"2-is_same_class" module.

The 1-my_list supplies the method is_same_class
"""


def is_same_class(obj, a_class):
    """
    returns True if the object is exactly an instance of the specified class
    """
    if type(obj) is a_class:
        return True
    else:
        return False
