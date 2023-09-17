#!/usr/bin/python3
"""Rectangle class module with tests."""
from models.base import Base


class Rectangle(Base):
    """Rectangle class with unittets."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialise Rectangle instance attribute.

        Args:
                width (:obj:`int`): width of rectangle.
                height (:obj:`int`): height of rectangle.
                x (:obj:`int`): x position.
                y (:obj:`int`): y position.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """`int` Get `width` of rectangle.

        Set,  set the width of a rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0 or value == 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """`int` Get height.

        Set `int` height.
        """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0 or value == 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Get `int` x positon.

        Set `int` x postion
        """
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Get `int` y positon.

        Set `int` y postion
        """
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("Y must be an integer")
        if value < 0:
            raise ValueError("Y must be >= 0")
        self.__y = value
