#!/usr/bin/python3
"""class student"""


class Student():
    """student class"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is not None:
            res = {k: self.__dict__[k] for k in self.__dict__.keys() & attrs}
            return res
        return self.__dict__

    def reload_from_json(self, json):
        for atr in json:
            self.__dict__[atr] = json[atr]
