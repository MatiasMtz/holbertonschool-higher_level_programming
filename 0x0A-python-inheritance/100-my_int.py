#!/usr/bin/python3
"""MyInt class which has == and != operators inverted"""


class MyInt(int):
    """Inherits from int"""
    def __init__(self, symbol):
        """instantiation of value"""
        self.symbol = symbol

    def __ne__(self, comparison):
        """sets true the comparison between unequal(__ne__) values"""
        if self.symbol is comparison:
            return True

    def __eq__(self, comparison):
        """sets false the comparison between equal(__eq__) values"""
        return False
