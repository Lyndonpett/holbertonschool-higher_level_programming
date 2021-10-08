#!/usr/bin/python3
"""This modules prints first and last name"""


def say_my_name(first_name, last_name=""):
    """Prints first and last name if they are a string"""

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")

    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is {0} {1}".format(first_name, last_name))
