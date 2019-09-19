#!/usr/bin/Python3
def print_sorted_dictionary(a_dictionary):

    if a_dictionary is not None:
        ikeys = sorted(a_dictionary.keys())

        for key in a_dictionary.keys():
            print("{:s}: {}".format(key, a_dictionary[key]))
