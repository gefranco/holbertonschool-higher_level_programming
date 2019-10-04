#!/usr/bin/python3
"""
"4-print_square" module.

The 4-print_square module supplies the function print_square
"""


def print_square(size):
    """
    prints a square with the character #
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        j = 0
        for j in range(size):
            print("#", end="")
        print()
