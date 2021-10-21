i#!/usr/bin/python3
"""Unittest for class Rectangle
"""
import unittest
import os
from io import StringIO
from unittest.mock import patch
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestRectangle(unittest.TestCase):
        """Testing Rectangle"""

        def tearDown(self):
            """Tears down obj count"""
            Base._Base__nb_objects = 0
            self.assertEqual(Base._Base__nb_objects, 0)

        def test_instance(self):
            """Test instantiation"""
            o1 = Rectangle(3, 2)
            o2 = Rectangle(8, 7, 0, 0, 12)
            with self.assertRaises(TypeError):
                o3 = Rectangle("string")
                o4 = Rectangle(None)
                o5 = Rectangle(float('inf'))
                o6 = Rectangle(9.5, 9.3)
                o7 = Rectangle(-8, 9)
                o8 = Rectangle()

            self.assertEqual(o1.id, 1)
            self.assertEqual(o1._Base__nb_objects, 1)
            self.assertEqual(o2.id, 12)
            self.assertEqual(o2._Base__nb_objects, 1)
