#!/usr/bin/python3
"""This function returns the list of available
    attributes and methods of an object
"""


def lookup(obj):
    """Returns list object

    Args:
        obj(type): Object

    Returns:
        Type: dir(obj)
    """

    return dir(obj)
