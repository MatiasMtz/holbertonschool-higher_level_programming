#!/bin/usr/python3
"""
Test for Rectangle class
"""

import unittest
from models.base import Base
from models.rectangle import Rectangle


class Testrec_instances(unittest.TestCase):
    """
    Test for Rectangle class
    """

    def test_isrec(self):
        self.assertIsInstance(Rectangle(10, 7), Base)

    def test_empty(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_w_priv(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(10, 7, 8, 2, 4).__width)

    def test_w_getter(self):
        rec = Rectangle(10, 7, 8, 2, 4)
        self.assertEqual(10, rec.width)

    def test_w_setter(self):
        rec = Rectangle(10, 7, 8, 2, 4)
        rec.width = 10
        self.assertEqual(10, rec.width)

    def test_h_pri(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(10, 7, 8, 2, 4).__height)

    def test_h_getter(self):
        rec = Rectangle(10, 7, 8, 2, 4)
        self.assertEqual(7, rec.height)

    def test_h_setter(self):
        rec = Rectangle(10, 7, 8, 2, 4)
        rec.height = 10
        self.assertEqual(10, rec.height)

    def test_y_pri(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(10, 7, 8, 2, 4).__y)

    def test_y_getter(self):
        rec = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(5, rec.y)

    def test_y_setter(self):
        rec = Rectangle(5, 7, 7, 5, 1)
        rec.y = 10
        self.assertEqual(10, rec.y)

    def test_x_pri(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(10, 7, 8, 2, 4).__x)

    def test_x_getter(self):
        rec = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(7, rec.x)

    def test_x_setter(self):
        rec = Rectangle(5, 7, 7, 5, 1)
        rec.x = 10
        self.assertEqual(10, rec.x)

    def test_single(self):
        with self.assertRaises(TypeError):
            Rectangle(10)

    def test_two(self):
        rec = Rectangle(10, 7)
        rec2 = Rectangle(4, 8)
        self.assertNotEqual(rec.id, rec2.id)

    def test_three(self):
        rec = Rectangle(10, 7, 2)
        rec2 = Rectangle(4, 8, 1)
        self.assertNotEqual(rec.id, rec2.id)

    def test_four(self):
        rec = Rectangle(10, 7, 2, 8)
        rec2 = Rectangle(4, 2, 1, 3)
        self.assertNotEqual(rec.id, rec2.id)

    def test_five(self):
        rec = Rectangle(10, 7, 2, 8, 4)
        rec2 = Rectangle(4, 2, 1, 3, 7)
        self.assertNotEqual(rec.id, rec2.id)

    def test_six(self):
        with self.assertRaises(TypeError):
            Rectangle(10, 7, 2, 8, 4, 1)


class Testw(unittest.TestCase):
    """Type class unittest instance for rectangle"""

    def test_none(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(None, 10)

    def test_str(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("Edward", 10)

    def test_float(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(10.2, 7)

    def test_dict(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({"a": 10, "b": 7}, 8)

    def test_list(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle([10, 7, 8], 8)

    def test_tuple(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle((10, 7, 8), 8)

    def test_nan(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(float('nan'), 10)

    def test_inf(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(float('inf'), 10)

    def test_set(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({10, 7, 8}, 8)

    def test_frozen(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(frozenset({10, 7, 8, 1}), 8)

    def test_negative(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-10, 7)

    def test_w(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 7)


if __name__ == '__main__':
    unittest.main()
