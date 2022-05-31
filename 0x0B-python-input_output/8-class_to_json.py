#!/usr/bin/python3
"""Defines a function that returns dictionary description of an object."""


def class_to_json(obj):
    """Returns dictionary description for JSON serilization of an object."""
    return vars(obj)
