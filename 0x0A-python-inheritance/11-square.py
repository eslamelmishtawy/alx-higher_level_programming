#!/usr/bin/python3
"""
Square Module
"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
    Square class
    """
    def __init__(self, size):
        """
        init square
        Args:
            size
        """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """
        implement area
        """
        return self.__size * self.__size

    def __str__(self):
        """
        print string
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
