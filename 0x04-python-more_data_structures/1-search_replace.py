#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """Search and replace an element in a list.

    Args:
        my_list: list of element to serch to
        search: element to search
        replace: a replacer element

    Returns:
            A new list[]
    """
    new_list = my_list[:]
    for index, value in enumerate(new_list):
        if value == search:
            new_list[index] = replace
    return new_list
