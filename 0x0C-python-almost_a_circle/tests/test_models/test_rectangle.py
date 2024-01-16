#!/usr/bin/python3
""" Test rectangle module """
import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle_init(unittest.TestCase):
    "Test Rectangle Init"
    def setUp(self):
        """ setup test """
        Base._Base__nb_objects = 0

    def test_rectangle(self):
        """ Test rectangle """
        r = Rectangle(2, 3)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)
        self.assertEqual(r.id, 1)

        r = Rectangle(2, 3, 5, 5, 12)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 5)
        self.assertEqual(r.y, 5)
        self.assertEqual(r.id, 12)

    def test_area(self):
        """ test area """
        new = Rectangle(2, 3)
        self.assertEqual(new.area(), 6)
