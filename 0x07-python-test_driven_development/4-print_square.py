#!/usr/bin/python3
"""This module prints a square using #"""


def print_square(size):
    """This function prints a square"""

    if type(size) is not int:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    if float(size) < 0:
        raise TypeError("size must be >= 0")

    for i in range(size):
        print(size * '#')
