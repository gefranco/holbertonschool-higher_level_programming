#!/usr/bin/python3
"""
"1-my_list" module.

The 1-my_list supplies the class MyList
"""


class MyList(list):
    """
    Class that inherits from  list
    """
    def print_sorted(self):
        """
        prints the list, but sorted (ascending sort)
        """
        copy = self[:]

        copy.sort()
        print(copy)
