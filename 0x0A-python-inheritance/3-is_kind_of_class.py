#!/usr/bin/python3
"""
"3-is_kind_of_class" module.

The 3-is_kind_of_class supplies the method is_kind_of_class
"""


def is_kind_of_class(obj, a_class):
    """
    returns True if the object is an instance of or a class that inherited from
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
