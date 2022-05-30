#!/usr/bin/python3
"""Verifies if the object is an instance of a class that inherited from
the specified class"""


def inherits_from(obj, a_class):
    """
    Args:
    obj (obj): object
    a_class (class): class"""
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    return False
