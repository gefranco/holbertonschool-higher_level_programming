#!/usr/bin/Python3
def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary.keys()) == 0:
        return None
    keys = list(a_dictionary.keys())

    best = 0
    key = ""
    for i in keys:
        if a_dictionary[i] >= best:
            best = a_dictionary[i]
            key = i

    return key
