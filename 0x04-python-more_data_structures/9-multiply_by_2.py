#!/usr/bin/Python3
def multiply_by_2(a_dictionary):
    if a_dictionary is not None:
        my_dictionary = {}

        for key in a_dictionary.keys():
            my_dictionary[key] = a_dictionary[key] * 2

        return my_dictionary
