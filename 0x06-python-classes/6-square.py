#!/usr/bin/python3

"""Square Class"""


class Square:
    """Square Class"""
    def __init__(self, size=0, position=(0, 0)):
        """Initialize square

        Args:
        size(int): size of square
        position (int, int): position on new square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        self.__position = position

    @property
    def position(self):
        """get position"""
        return (self.__position)

    @position.setter
    def position(self, value):
        """set position"""
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

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
        for i in range(self.__position[1]):
            print()
        for i in range(self.__size):
            for j in range(self.__position[0]):
                print(" ", end='')
            print("#" * (self.__size))
