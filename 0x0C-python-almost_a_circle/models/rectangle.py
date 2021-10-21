#!/usr/bin/python3
"""This module defines class Rectangle"""


from models.base import Base


class Rectangle(Base):
    """Defining Rectangle that inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Init for rect, only taking id from parent"""
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
        """Defning width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setting width"""
        self.integerValidator("width", value)
        self.__width = value

    @property
    def height(self):
        """Defining height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setting height"""
        self.integerValidator("height", value)
        self.__height = value

    @property
    def x(self):
        """defning x"""
        return self.__x

    @x.setter
    def x(self, value):
        """setting x"""
        self.xyValidator("x", value)
        self.__x = value

    @property
    def y(self):
        """defining y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Y setter"""
        self.xyValidator("y", value)
        self.__y = value

    def area(self):
        """Area for rectangle"""
        return self.__height * self.__width

    def display(self):
        """Printing for rectangle"""
        for row in range(self.__y):
            print("")
        for col in range(self.__height):
            print(" "*self.__x, end="")
            print("#"*self.__width)

    def __str__(self):
        """Str of rectangle"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """Updating the function"""
        Attributes = ['id', 'width', 'height', 'x', 'y']
        if args and len(args) != 0:
            for key in range(len(args)):
                setattr(self, Attributes[key], args[key])

        else:
            for item in kwargs:
                setattr(self, item, kwargs[item])

    def to_dictionary(self):
        """creating dic for rectangle"""
        Dic = {'id': self.id, 'width': self.width,
               'height': self.height, 'x': self.x, 'y': self.y}
        return Dic
