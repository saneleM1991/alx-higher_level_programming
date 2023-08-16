#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """Delete a key in a dictionary.

    Args:
        a_dictionary: Dictionary to delete key from
        key: Key to delete

    Returns:
            Modified dictionary
    """
    if a_dictionary.get(key) is not None:
        del a_dictionary[key]
    return (a_dictionary)
