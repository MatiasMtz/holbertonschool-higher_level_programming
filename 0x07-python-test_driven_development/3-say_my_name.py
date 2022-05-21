#!/usr/bin/python3
"""Module that prints My name is <first name> <last name>"""


def say_my_name(first_name, last_name=""):
    """
    Args:
    first_name (str): First parameter to print
    last_name (str): Second parameter to print
    """
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    elif type(last_name) != str:
        raise TypeError("last_name must be a string")
    else:
        print("My name is {} {}".format(first_name, last_name))
