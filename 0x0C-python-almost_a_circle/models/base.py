#!/usr/bin/python3
"""Base class for future class module with tests."""


class Base:
    """Base class to mantain id for its subclass."""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialising base class members.

        Args:
        id (:obj:`int`, optional): instance member.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
