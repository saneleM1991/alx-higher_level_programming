"""Rectangle test suites module."""
import unittest
from models.rectangle import Rectangle


class TestingRectangle(unittest.TestCase):
    """Test rectangle test suites."""

    def test_width_setter_and_getter(self):
        """test width setter. """
        obj = Rectangle(10, 2)
        self.assertEqual(obj.width, 10)

    def test_height_setter_and_getter(self):
        """Test height setter and getter."""
        obj = Rectangle(10, 2)
        self.assertEqual(obj.height, 2)

    def test_x_setter_and_getter(self):
        """test x setter and getter."""
        obj = Rectangle(10, 2, 11, 23)
        self.assertEqual(obj.x, 11)

    def test_y_setter_and_getter(self):
        """test y setter and getter."""
        obj = Rectangle(10, 2, 11, 23)
        self.assertEqual(obj.y, 23)

    def test_x_with_default_value(self):
        """test x with default value."""
        obj = Rectangle(10, 2)
        self.assertEqual(obj.x, 0)

    def test_y_with_default_value(self):
        """test y with default value."""
        obj = Rectangle(10, 2)
        self.assertEqual(obj.y, 0)

    def test_id_value_with_none(self):
        """test id value with none param."""
        obj = Rectangle(10, 2)
        self.assertEqual(obj.id, 2)

    def test_id_value_with_value(self):
        """test id value with value param."""
        obj = Rectangle(10, 2, id=34)
        self.assertEqual(obj.id, 34)
