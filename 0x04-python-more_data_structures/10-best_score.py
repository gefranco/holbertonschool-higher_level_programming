#!/usr/bin/Python3
def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary.keys()) == 0:
        return None
    keys = list(a_dictionary.keys())
    keys.sort()
    return keys[len(keys)-1]
