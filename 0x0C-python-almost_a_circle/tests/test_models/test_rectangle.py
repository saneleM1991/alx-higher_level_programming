"""Rectangle test suites module."""
import unittest
from models.rectangle import Rectangle


class TestingRectangle(unittest.TestCase):
    """Test rectangle test suites."""

    def test_width_and_height_setter_and_getter(self):
        """test width and heigth setter and getter. """
        obj = Rectangle(12, 2)
        self.assertEqual(obj.width, 12)
        self.assertEqual(obj.height, 2)
        with self.assertRaises(ValueError):
            obj1 = Rectangle(0, 0)
            obj2 = Rectangle(-30, -12)
        with self.assertRaises(TypeError):
            obj1 = Rectangle("f", "ff0")

    def test_x_and_y_setter_and_getter(self):
        """test x setter and getter."""
        obj = Rectangle(10, 2, 11, 23)
        self.assertEqual(obj.x, 11)
        self.assertEqual(obj.y, 23)
        with self.assertRaises(ValueError):
            obj1 = Rectangle(2, 3, -1, -34)
        with self.assertRaises(TypeError):
            obj1 = Rectangle(2, 3, "r", "h")

    def test_x_and_y_with_default_value(self):
        """test x with default value."""
        obj = Rectangle(10, 2)
        self.assertEqual(obj.x, 0)
        self.assertEqual(obj.y, 0)

    def test_id_value_with_default_value(self):
        """test id value with none param."""
        obj = Rectangle(10, 2)
        self.assertEqual(obj.id, 1)

    def test_id_value_with_value(self):
        """test id value with value param."""
        obj = Rectangle(10, 2, id=34)
        self.assertEqual(obj.id, 34)
