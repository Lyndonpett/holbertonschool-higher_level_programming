#!/usr/bin/python3
"""Defining class BaseGeometry"""


class BaseGeometry:
    "Raises exception for area"

    def area(self):
        raise Exception("area() is not implemented")

    """Validates value"""

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
