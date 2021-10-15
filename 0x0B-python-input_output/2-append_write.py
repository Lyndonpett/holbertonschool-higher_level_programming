#!/usr/bin/python3
"""This module appends a string and returns number of characters added"""


def append_write(filename="", text=""):
    """Appends text to a file and returns num of chars appended"""

    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
