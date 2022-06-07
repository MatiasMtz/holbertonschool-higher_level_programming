#!/usr/bin/python3
"""Base class of all other classes in this project"""
import json


class Base:
    """Class that voids duplicating the same code"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Instantiation of Base attributes
        Args:
        id (int): Object identification"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Function that returns the JSON representation of an object
        Args:
        list_dictionaries (list): List of dictionaries"""
        if list_dictionaries is None or list_dictionaries == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Function that writes the JSON string representation of list_objs
        Args:
        list_objs (list): List of instances who inherits of Base"""
        objectList = []
        filename = cls.__name__ + ".json"
        if list_objs is not None:
            for obj in list_objs:
                objectList.append(obj.to_dictionary())
        with open(filename, "w") as file:
            file.write(cls.to_json_string(objectList))

    @staticmethod
    def from_json_string(json_string):
        """Function that returns the list of the JSON string representation
        Args:
        json_string (string): Represents a list of dictionaries"""
        aDict = []
        if json_string is None or len(json_string) == 0:
            return aDict
        aDict = json.loads(json_string)
        return aDict

    @classmethod
    def create(cls, **dictionary):
        """Function that returns an instance with all attributes already set
        Args:
        dictionary (dict): can be treated as double pointer to a dictionary"""
        if cls.__name__ == "Rectangle":
            newInstance = cls(1, 1)
        elif cls.__name__ == "Square":
            newInstance = cls(1)
        cls.update(newInstance, **dictionary)
        return newInstance

    @classmethod
    def load_from_file(cls):
        """Function that returns a list of instances
        Args:
        cls: current class using this method"""
        instanceList = []
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as file:
                instanceList = cls.from_json_string(file.read())
                for obj, value in enumerate(instanceList):
                    instanceList[obj] = cls.create(**instanceList[obj])
        except FileNotFoundError:
            pass
        return instanceList
