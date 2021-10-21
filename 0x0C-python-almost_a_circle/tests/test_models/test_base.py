#!/usr/bin/python3
"""Unittest for class Base
"""
import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
        """Testing Base"""

        def tearDown(self):
            """Tears down obj count"""
            Base._Base__nb_objects = 0
            self.assertEqual(Base._Base__nb_objects, 0)

        def test_instance(self):
            """Test instantiation"""

            o1 = Base()
            o2 = Base(9)
            o3 = Base(9.5)
            o4 = Base(float('inf'))
            o5 = Base("string")
            o6 = Base(["list", 4, 2.5])
            o7 = Base(None)         
