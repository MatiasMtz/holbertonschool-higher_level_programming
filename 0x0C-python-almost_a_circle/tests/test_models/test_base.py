"""
Unittests for the Base class
"""

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):

    def test_ids(self):
        """
        Test id
        """

        Base._Base__nb_objects = 0
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base(12)
        self.assertEqual(b2.id, 12)
        b3 = Base(0)
        self.assertEqual(b3.id, 0)
        b4 = Base(-3)
        self.assertEqual(b4.id, -3)
        b5 = Base()
        self.assertEqual(b5.id, 2)

    def test_to_json_string(self):
        """
        test to_json_string method
        """

        Base._Base__nb_objects = 0
        obj = Base(33)
        dic = obj.__dict__

        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(Base.to_json_string(dic), '{"id": 33}')

    def test_save_to_file(self):
        """
        test save_to_file method
        """
        Base._Base__nb_objects = 0
        obj = Base(33)

        Base.save_to_file(None)
        with open("Base.json", "r") as f:
            read = f.read()
            new_list = Base.from_json_string(read)
            self.assertEqual(new_list, [])

        Base._Base__nb_objects = 0
        rec = Rectangle(1, 2, 3, 4, 5)
        Rectangle.save_to_file([rec])
        with open("Rectangle.json", "r") as f:
            read = f.read()
            new_list = Base.from_json_string(read)
            self.assertEqual(new_list, [{'id': 5, 'width': 1,
                                        'height': 2, 'x': 3, 'y': 4}])

        Base._Base__nb_objects = 0
        sq = Square(1, 2, 3, 4)
        Square.save_to_file([sq])
        with open("Square.json", "r") as f:
            read = f.read()
            new_list = Base.from_json_string(read)
            self.assertEqual(new_list, [{'id': 4, 'size': 1, 'x': 2, 'y': 3}])

    def test_from_json_string(self):
        """
        test from_json_string method
        """

        Base._Base__nb_objects = 0
        obj = Base(33)
        string = [{'id': 33}]

        self.assertEqual(string, [{'id': 33}])

    def test_load_form_file(self):
        """
        test load_from_file method
        """

        Base._Base__nb_objects = 0
        obj = Base(33)

        Base.save_to_file(None)
        new_list = Base.load_from_file()
        self.assertEqual(new_list, [])

    def test_create(self):
        """
        test create method
        """

        rec = Rectangle(1, 2, 3, 4, 5)
        rec_dict = rec.to_dictionary()
        rec_new = Rectangle.create(**rec_dict)
        self.assertEqual("[Rectangle] (5) 3/4 - 1/2", str(rec))
        self.assertEqual("[Rectangle] (5) 3/4 - 1/2", str(rec_new))

        sq = Square(1, 2, 3, 4)
        sq_dict = sq.to_dictionary()
        sq_new = Square.create(**sq_dict)
        self.assertEqual("[Square] (4) 2/3 - 1", str(sq))
        self.assertEqual("[Square] (4) 2/3 - 1", str(sq_new))
