"""Base class model tests."""
import unittest
from models.base import Base


class TestBaseClass(unittest.TestCase):
    """Test suite for base class."""

    def test_is_type_of_base(self):
        """Test for instance type."""
        base = Base()
        self.assertIsInstance(base, Base)

    def test_instance_base_has_id_attr(self):
        """Checking if instance member id present."""
        obj = Base()
        self.assertIn("id", dir(obj))

    def test_class_base_has_nbobjects_attr(self):
        """Checking if class member __nb_objects present."""
        self.assertIn("_Base__nb_objects", dir(Base))

    def test_id_value_one(self):
        """Test id value one. """
        obj = Base()
        self.assertEqual(obj.id, 1)

    def test_id_value_twoo(self):
        """Test id value twoo. """
        obj = Base()
        self.assertEqual(obj.id, 2)

    def test_check_value_of_id(self):
        """Test id value three. """
        obj = Base(10)
        self.assertEqual(obj.id, 10)

    def test_id_nagetive_value(self):
        """Test id value three. """
        obj = Base(-10)
        self.assertEqual(obj.id, -10)
