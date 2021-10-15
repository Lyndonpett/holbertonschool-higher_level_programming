#!/usr/bin/python3
"""This module defines class Student"""


class Student:
    """Adding definition to class"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        StringAttrs = {}

        if attrs is not None:
            for key in attrs:
                if key in self.__dict__:
                    StringAttrs[key] = self.__dict__[key]
            return StringAttrs
        else:
            return vars(self)

    def reload_from_json(self, json):
        for i in json:
            setattr(self, i, json[i])
