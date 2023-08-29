#!/usr/bin/python3
"""Square module that has a class to create square object."""


class Square:
    """An empty square class."""

    def __init__(self, size=0):
        """Init method for the square class.

        Args:
            size (:obj:`int`, optional): size of a square.

        Raises:
            TypeError: if `size` is not an `int`.
            ValueError: If `size` is < 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Get the area of a square.

        Returns:
            Area (`int`) : size * size.
        """
        return self.__size * self.__size
