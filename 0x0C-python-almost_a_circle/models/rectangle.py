#!/usr/bin/python3
"""
rectangle module
"""


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super.__init__(id)

    @property
    def width(self):
        """ width getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ width setter """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ height getter """
        return self.__height

    @height.setter
    def height(self, value):
        """ height setter """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ x getter """
        return self.__x

    @x.setter
    def x(self, value):
        """ x setter """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ y getter """
        return self.__y

    @y.setter
    def y(self, value):
        """ y setter """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ return area """
        return self.width * self.height

    def display(self):
        """ display rectangle """
        rectangle = self.y * "\n"
        for i in range(self.height):
            rectangle += (" " * self.x)
            rectangle += ("#" * self.width) + "\n"

        print(rectangle, end='')

    def __str__(self):
        """ str method """
        return "[Rectangle] ({}) {}/{} - {}/{}" \
            .format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """ update method """
        if args is not None and len(args) is not 0:
            list_atr = ['id', 'width', 'height', 'x', 'y']
            for i in range(len(args)):
                setattr(self, list_atr[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ dict method """
        return {'id': self.id,
                'width': self.width,
                'height': self.height,
                'x': self.x,
                'y': self.y}
