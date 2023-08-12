#!/usr/bin/python3


def multiple_returns(sentence):
    """Returns the length of a string and its first character.

    Args:
                sentence: string to get lenght and char from

    Return:
                tuple (lenght | first char)
    """
    if sentence == "":
        return (0, None)
    return (len(sentence), sentence[0])
