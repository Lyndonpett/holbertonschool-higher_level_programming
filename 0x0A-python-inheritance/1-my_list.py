#!/usr/bin/python3
"""Class that prints the a sorted list"""


class MyList(list):
    """prints a sorted list"""

    def __init__(self):
        super().__init__()

    def print_sorted(self):
        print(sorted(self))
