#!/usr/bin/Python3
def print_sorted_dictionary(a_dictionary):

    if a_dictionary is not None:
        sorted(a_dictionary)

        for key in a_dictionary:
            print("{:s},{}".format(key, a_dictionary[key]))
