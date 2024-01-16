#!/usr/bin/python3
""" 0-main """
from models.base import Base
from models.rectangle import Rectangle

if __name__ == "__main__":

    b1 = Base()

    b2 = Base(12)

    b3 = Base(None)

    b5 = Base(None)
    print(b1.id)
    print(b2.id)
    print(b3.id)
    print(b5.id)
    r1 = Rectangle(10, 2)
    print(r1.id)

    r2 = Rectangle(2, 10)
    print(r2.id)

    r3 = Rectangle(10, 2, 0, 0, 12)
    print(r3.id)
