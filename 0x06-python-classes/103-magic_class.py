#!/usr/bin/python3
"""MagicClass"""


class MagicClass:
    """circle representation"""

    def __init__(self, radius=0):
        """
        Initialize a MagicClass
        radius float or int : Is the radius of the new MagicClass
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Return the area of the MagicClass"""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """Return The circumference of the MagicClass"""
        return (2 * math.pi * self.__radius)
