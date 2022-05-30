#!/usr/bin/python3
"""Function that adds a new attribute to an object if it’s possible"""


def add_attribute(obj, attribute, value):
    """
    Args:
    obj (obj): object
    attribute: attribute to be added
    value: value of the attribute"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attribute, value)
