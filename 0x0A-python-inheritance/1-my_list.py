#!/usr/bin/python3
"""Class MyList that inherits from list."""


class MyList(list):
    """Inherits from list"""
    def print_sorted(self):
        """Prints the sorted list"""
        print(sorted(self))
