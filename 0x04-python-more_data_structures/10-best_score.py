#!/usr/bin/Python3
def best_score(a_dictionary):
    if a_dictionary is not None:
        keys = list(a_dictionary.keys())
        keys.sort()
        return keys.pop()
