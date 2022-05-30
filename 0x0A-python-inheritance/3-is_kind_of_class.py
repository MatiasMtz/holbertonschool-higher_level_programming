#!/usr/bin/python3
"""Verifies if the object is an instance of, or if the object is an instance
of a class that inherited from, the specified class"""


def is_kind_of_class(obj, a_class):
    """
    Args:
    obj (obj): object
    a_class (class): class"""
    if isinstance(obj, a_class):
        return True
    return False
