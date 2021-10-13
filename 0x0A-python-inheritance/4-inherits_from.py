#!/usr/bin/python3
"""Checks if object is an instance of an inherited class"""


def inherits_from(obj, a_class):
    """Returns true if is instance of an inherited class"""

    return(issubclass(type(obj), a_class) and type(obj) is not a_class)
