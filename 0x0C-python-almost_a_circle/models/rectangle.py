#!/usr/bin/python3
"""This module defines class Rectangle"""


from models.base import Base


class Rectangle(Base):
    """Defining Rectangle that inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)

        self.integerValidator("width", width)
        self.__width = width
        self.integerValidator("height", height)
        self.__height = height
        self.xyValidator("x", x)
        self.__x = x
        self.xyValidator("y", y)
        self.__y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.integerValidator("width", value)
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.integerValidator("height", value)
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.xyValidator("x", value)
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.xyValidator("y", value)
        self.__y = value
