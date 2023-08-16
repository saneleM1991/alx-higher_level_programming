#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    """Replace or add key/value pairs in a dictionary.

    Args:
        a_dictionary: Dictionary to update or add value
        key: string key
        value: value

    Returns:
            A new dictionary {}
    """
    a_dictionary[key] = value
    return (a_dictionary)
