#!/usr/bin/python3
"""Verify if the object is exactly an instance of the specified class"""


def is_same_class(obj, a_class):
    """
    Args:
    obj (obj): object
    a_class: class"""
    if type(obj) is a_class:
        return True
    return False
