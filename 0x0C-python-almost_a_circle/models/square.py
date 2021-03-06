#!/usr/bin/python3
"""This module defines class Square"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Defining Square class inherited from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """__init__ from parent class"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Str format for square"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """Defining size"""
        return self.width

    @size.setter
    def size(self, value):
        """size setter"""
        self.integerValidator("width", value)
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Handling updating"""
        Attributes = ['id', 'size', 'x', 'y']
        if args and len(args) != 0:
            for key in range(len(args)):
                setattr(self, Attributes[key], args[key])

        else:
            for item in kwargs:
                setattr(self, item, kwargs[item])

    def to_dictionary(self):
        """creating a dic for square"""
        Dic = {'id': self.id, 'size': self.width, 'x': self.x, 'y': self.y}
        return Dic
