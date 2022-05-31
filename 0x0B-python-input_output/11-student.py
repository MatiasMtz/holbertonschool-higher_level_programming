#!/usr/bin/python3
"""Student to JSON with filter"""


class Student:
    """class Student that defines a student"""

    def __init__(self, first_name, last_name, age):
        """Instantiation of first name, last name and age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance"""
        if attrs is None:
            return self.__dict__
        else:
            tmp = {}
            for item in attrs:
                if type(item) != str:
                    return self.__dict__
                if item in self.__dict__.keys():
                    tmp[item] = self.__dict__[item]
            return tmp

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance"""
        for item in json:
            self.__dict__[item] = json[item]
