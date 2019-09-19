#!/usr/bin/python3


def search_replace_number(number, search, replace):
    if number == search:
        return replace
    else:
        return number


def search_replace(my_list, search, replace):
    if my_list is not None:

        new_list = [search_replace_number(x, search, replace) for x in my_list]

        return new_list
