#!/usr/bin/python3
"""
"100-my_int" module.

The 100-my_int supplies the class MyInt
"""


class MyInt(int):
    """
    class MyInt, inherits from int
    """
    def __eq__(self, value):
        return super().__ne__(value)

    def __ne__(self, value):
        return super().__eq__(value)
