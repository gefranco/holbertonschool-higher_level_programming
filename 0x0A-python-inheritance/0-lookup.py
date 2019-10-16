#!/usr/bin/python3
"""
"0-lookup" module.

The 0-lookup module supplies the function lookup
"""


def lookup(obj):
    """
    Returns the list of available attributes and methods of an object
    """
    return dir(obj)
