#!/usr/bin/Python3
def complex_delete(a_dictionary, value):
    if a_dictionary is None or len(a_dictionary.keys()) == 0:
        return None
    keys = list(a_dictionary.keys())

    for i in keys:
        if a_dictionary[i] == value:
            del a_dictionary[i]

    return a_dictionary
