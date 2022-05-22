#!/usr/bin/python3
"""Unittests for the function def max_integer(list=[]):"""


import unittest
max_integer = __import__('6-max_integer').max_integer

class findMaxInt(unittest.TestCase):
    """Class that contains tests for max_integer()"""
    def testPositives(self)
    """Tests for positive numbers"""
    intList = [10, 11, 12, 13]
    self.assertEqual(max_integer(intlist), 13)
    intList = [1]
    self.assertEqual(max_integer(intlist), 1)
    intList = [[1, 2, 3][3, 2, 1]]
    self.assertEqual(max_integer(intlist), [3, 2, 1])
    intList = [[[[[5, 4, 3, 2, 1]]]]]
    self.assertEqual(max_integer(intlist), 5)
    intlist = ["a", "z"]
    self.assertEqual(max_integer(intlist), z)
