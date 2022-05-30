#!/usr/bin/python3
"""function that returns the list of available attributes and methods of
an object"""


def lookup(obj):
    """
    obj (obj): object where may lookup the list of attributes and methods"""
    methods = []
    for attribute in dir(obj):
        methods.append(attribute)
    return methods
