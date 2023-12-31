#!/usr/bin/python3
"""
Test Base Class Module
"""
import unittest
from models.base import Base


class TestBase_init(unittest.TestCase):
    """
    Testing class for Base instantiation
    """
    @classmethod
    def setUpClass(cls):
        print("setUpClass")

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass")

    def test_none_integer_id(self):
        b1 = Base("test")
        self.assertEqual(b1.id, "test")
        b2 = Base(1.1)
        self.assertEqual(b2.id, 1.1)

    def test_correct_ids(self):
        b1 = Base()
        b2 = Base(12)
        b3 = Base()
        b4 = Base(None)
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 12)
        self.assertEqual(b3.id, 2)
        self.assertEqual(b4.id, 3)
        b1.id = 203
        self.assertEqual(b1.id, 203)

    def test_none_id(self):
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, 4)
        self.assertEqual(b2.id, 5)
