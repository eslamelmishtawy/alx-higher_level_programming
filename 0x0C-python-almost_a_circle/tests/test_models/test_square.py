#!/usr/bin/python3
""" Test square module """
import unittest
from models.base import Base


class TestSquar_Init(unittest.TestCase):
    """ Test Square class """

    def setUp(self):
        """ Setup test """
        Base._Base__nb_objects = 0

    def test_square(self):
        """ Test square """
        s = Square(5)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.width, 5)
        self.assertEqual(s.height, 5)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 0)
        self.assertEqual(s.id, 1)

        new = Square(5, 5, 5, 12)
        self.assertEqual(new.size, 5)
        self.assertEqual(new.width, 5)
        self.assertEqual(new.height, 5)
        self.assertEqual(new.x, 5)
        self.assertEqual(new.y, 5)
        self.assertEqual(new.id, 12)

    def test_area(self):
        """ test area """
        s = Square(5)
        self.assertEqual(s.area(), 25)
