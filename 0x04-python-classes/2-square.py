#!/usr/bin/python3
"""The use of this module is to create a class named Square"""


class Square:
    """This define class and instantiates a private attribute"""

    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")

        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        squareArea = self.__size * self.__size
        return squareArea
