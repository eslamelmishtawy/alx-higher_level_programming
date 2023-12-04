#!/usr/bin/python3
"""
Base Geometry Module
"""


class BaseGeometry():
    """
    Base Geometry Class
    """
    def area(self):
        """
        raise exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        integer validator
        Args:
            name: name
            value: value
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
