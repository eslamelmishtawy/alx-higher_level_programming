#!/usr/bin/python3
""" 0-main """
from models.base import Base

if __name__ == "__main__":

    b1 = Base()

    b2 = Base(12)

    b3 = Base(None)

    b5 = Base(None)
    print(b1.id)
    print(b2.id)
    print(b3.id)
    print(b5.id)
