"""
Unittest for Square class
"""

import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """
    Tests ractangle class
    """

    def test_attributes(self):
        """
        Test attributes
        """
        sq = Square(1, 2, 3, 4)
        self.assertEqual(sq.size, 1)
        self.assertEqual(sq.x, 2)
        self.assertEqual(sq.y, 3)
        self.assertEqual(sq.id, 4)

        sq = Square(1)
        self.assertEqual(sq.size, 1)
        self.assertEqual(sq.x, 0)
        self.assertEqual(sq.y, 0)
        self.assertEqual(sq.id, 4)

    def test_Errors(self):
        """
        Test Errors
        """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("Holberton", 2, 3, 4)
            Square([1], 2, 3, 4)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, "School", 3, 4)
            Square(1, (2), 3, 4)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, True, 4)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-3, 2, 3, 4)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(1, -2, 3, 4)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(1, 2, -3, 4)

    def test_area(self):
        """
        Test area method
        """

        sq = Square(1)
        self.assertEqual(sq.area(), 1)
        sq = Square(6, 3, 4, 5)
        self.assertEqual(sq.area(), 36)

    def test_print(self):
        """
        Test __str__ method
        """
        sq = Square(1, 3, 4, 5)
        self.assertEqual(str(sq), '[Square] (5) 3/4 - 1')

    def test_update(self):
        """
        Test update method
        """
        sq = Square(1, 2, 3, 4)
        sq.update(3, 3, 3, 3)
        self.assertEqual(str(sq), '[Square] (3) 3/3 - 3')
        sq.update()
        self.assertEqual(str(sq), '[Square] (3) 3/3 - 3')
        sq.update(id=2, x=2, y=2, size=2)
        self.assertEqual(str(sq), '[Square] (2) 2/2 - 2')
        sq.update(id=3)
        self.assertEqual(str(sq), '[Square] (3) 2/2 - 2')

    def test_to_dictionary(self):
        """
        to_dictionary method
        """

        sqdic = Square(1, 2, 3, 4).to_dictionary()
        self.assertEqual(type(sqdic), dict)
