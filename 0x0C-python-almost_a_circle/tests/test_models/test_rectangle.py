"""
Unittest for rectangle class
"""

import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """
    Tests ractangle class
    """

    def test_attributes(self):
        """
        Test attributes
        """
        rec = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(rec.width, 1)
        self.assertEqual(rec.height, 2)
        self.assertEqual(rec.x, 3)
        self.assertEqual(rec.y, 4)
        self.assertEqual(rec.id, 5)

        rec = Rectangle(1, 2)
        self.assertEqual(rec.width, 1)
        self.assertEqual(rec.height, 2)
        self.assertEqual(rec.x, 0)
        self.assertEqual(rec.y, 0)
        self.assertEqual(rec.id, 2)

    def test_Errors(self):
        """
        Test Errors
        """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("Holberton", 2, 3, 4, 5)
            Rectangle([1], 2, 3, 4, 5)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, "School", 3, 4, 5)
            Rectangle(1, (2), 3, 4, 5)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, "Python", 4, 5)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, True, 5)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-3, 2, 3, 4, 5)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, 0, 3, 4, 5)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(1, 2, -3, 4, 5)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(1, 2, 3, -4, 5)

    def test_area(self):
        """
        Test area method
        """
        rec = Rectangle(1, 2)
        self.assertEqual(rec.area(), 2)
        rec2 = Rectangle(6, 6, 3, 4, 5)
        self.assertEqual(rec2.area(), 36)

    def test_print(self):
        """
        Test __str__ method
        """
        rec = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(str(rec), '[Rectangle] (5) 3/4 - 1/2')

    def test_update(self):
        """
        Test update method
        """
        rec = Rectangle(1, 2, 3, 4, 5)
        rec.update(3, 3, 3, 3, 3)
        self.assertEqual(str(rec), '[Rectangle] (3) 3/3 - 3/3')
        rec.update()
        self.assertEqual(str(rec), '[Rectangle] (3) 3/3 - 3/3')
        rec.update(id=2, x=2, y=2, width=2, height=2)
        self.assertEqual(str(rec), '[Rectangle] (2) 2/2 - 2/2')
        rec.update(id=3)
        self.assertEqual(str(rec), '[Rectangle] (3) 2/2 - 2/2')

    def test_to_dictionary(self):
        """
        to_dictionary method
        """

        recdic = Rectangle(1, 2, 3, 4, 5).to_dictionary()
        self.assertEqual(type(recdic), dict)
