#!/usr/bin/python3
"""
"4-inherits_from" module.

The 4-inherits_from supplies the method inherits_from
"""


def inherits_from(obj, a_class):
    """
    returns True if the object inherited from the specified class
    """
    if isinstance(obj, a_class) and type(obj) is not a_class:

        return True
    else:
        return False
