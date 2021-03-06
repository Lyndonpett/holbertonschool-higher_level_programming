#!/usr/bin/python3
"""The use of this module is to create a class named Square"""


class Square:
    """This define class and instantiates a private attribute"""

    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")

        elif value < 0:
            raise ValueError("size must be >= 0")

        else:
            self.__size = value

    def area(self):
        squareArea = self.__size * self.__size
        return squareArea

    def my_print(self):
        if self.__size is 0:
            print()
        for x in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print()
