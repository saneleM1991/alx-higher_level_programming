#!/usr/bin/python3
"""Rectangle Class Module Defination."""


class Rectangle:
    """Rectangle class."""

    def __init__(self, width=0, height=0):
        """Initialize instance attribute.

        Args:
            with (int): width.
            height (int): height.

        Raises:
            TypeError: if `width` OR `height` are not int.
            ValueError: if `width` OR `height` < 0
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """`int` Getting width of rectangle.

        Set with will raise exeption if `width` is not
        `int` and if `width` < 0
        """
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """`int` Returning the heigh of a rectanglr.

        Setting height will raise exeption if height
        is not an int and if `value` < 0
        """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Get area of a rectangle.

        Returns:
                `int` Area of rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """Get perimeter of a rectangle.

        Returns:
                `int` Perimeter of rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
