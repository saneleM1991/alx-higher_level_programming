#!/usr/bin/python3
"""Square module that has a class to create square object."""


class Square:
    """An empty square class."""

    def __init__(self, size=0, position=(0, 0)):
        """Init method for the square class.

        Args:
            size (:obj:`int`, optional): size of a square.
            position (:obj:`tuple`, optional): position.

        Raises:
            TypeError: if `size` is not an `int`.
            ValueError: If `size` is < 0.
            TypeError: if position is not tuple of 2 `int`.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        self.position = position

    def area(self):
        """Get the area of a square.

        Returns:
            Area (`int`) : size * size.
        """
        return self.__size * self.__size

    @property
    def size(self):
        """:obj:`int`: Returns `size` of a square.

        Setter raise an `TyprError` if `value` is not int
        or raise `ValueError` if `value` < 0
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """:obj:`tuple`: Returns tuple of twoo integers.

        Setter raises an TypeError if value is not tuple of twoo `int`.
        """
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2 and value[0] < 0 and value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """Prints the square with the character `#`."""
        if self.__size == 0:
            print("")
            return
        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
