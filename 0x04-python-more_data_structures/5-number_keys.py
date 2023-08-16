#!/usr/bin/python3

def number_keys(a_dictionary):
    """Get number of keyin a dictionary.

    Args:
                a_dictionary: dictionary to get key form

    Return:
                Number of keys in a dictionary
    """
    if isinstance(a_dictionary, dict):
        return len(a_dictionary.keys())
