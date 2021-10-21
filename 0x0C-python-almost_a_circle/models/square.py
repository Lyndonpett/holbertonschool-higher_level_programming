#!/usr/bin/python3
"""This module defines class Square"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Defining Square class inherited from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.integerValidator("width", value)
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        Attributes = ['id', 'size', 'x', 'y']
        if args and len(args) != 0:
            for key in range(len(args)):
                setattr(self, Attributes[key], args[key])

        else:
            for item in kwargs:
                setattr(self, item, kwargs[item])

    def to_dictionary(self):
        Dic = {'id': self.id, 'size': self.width, 'x': self.x, 'y': self.y}
        return Dic
