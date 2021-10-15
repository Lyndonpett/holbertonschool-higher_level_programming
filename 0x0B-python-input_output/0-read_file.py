#!/usr/bin/python3
"""This module reads a file and prints it to stdout"""


def read_file(filename=""):
    """Reads a text file"""

    with open(filename, encoding="UTF-8") as f:
        print(f.read(), end="")
