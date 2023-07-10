#!/usr/bin/python3
"""
Module of the class MyInt that inherits from int
"""


class MyInt(int):
    """
    MyInt is a rebel. MyInt has == and != operators inverted
    """

    def __init__(self, value):
        """
        Initializing value
        """
        self.value = value

    def __eq__(self, other):
        """
        Returns invert of ==
        """
        return self.value != other

    def __ne__(self, other):
        """
        Returns invert of !=
        """
        return self.value == other
