#!/usr/bin/python3
"""Class MyList that inherits from list."""


class MyList(list):
    """Prints the sorted list"""
    def print_sorted(self):
        """Public instance method that prints the sorted list"""
        return sorted(self)
