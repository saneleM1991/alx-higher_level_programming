#!/usr/bin/python3
"""Lookup module file with python"""


def lookup(obj):
    """Lookup object props and methods.

    Args:
        obj (:obj:`any`): object to look.

    Returns:
        `lis[]` of props and  methods of `obj`.
    """
    return dir(obj)
