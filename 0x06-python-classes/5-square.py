#!/usr/bin/python3

"""Square Class"""


class Square:
    """Square Class"""
    def __init__(self, size=0):
        """Initialize square

        Args:
        size(int): size of square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """get size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """set size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """get square area"""
        return (self.__size * self.__size)

    def my_print(self):
        """print square with #"""
        if self.__size <= 0:
            print()
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end='')
            print()
