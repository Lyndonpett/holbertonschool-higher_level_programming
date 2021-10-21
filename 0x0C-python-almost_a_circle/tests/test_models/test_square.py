#!/usr/bin/python3
"""This Module is for testing the Square Class"""


import unittest
import pep8
from models.square import Square


class TestSquare(unittest.TestCase):
    """Testing the Square class"""

    # Testing using ClassMethod to set up square.

    @classmethod
    def setUpClass(cls):
        cls.s1 = Square(10)
        cls.s2 = Square(5, 10, 5)
        cls.s3 = Square(50)

    @classmethod
    def tearDownClass(cls):
        del cls.s1
        del cls.s2
        del cls.s3

    # Testing __init__ values are correct

    def testInstantation(self):
        self.assertEqual(self.s1.id, 8)
        self.assertEqual(self.s1.width, 10)
        self.assertEqual(self.s1.height, 10)
        self.assertEqual(self.s1.x, 0)
        self.assertEqual(self.s1.y, 0)

        self.assertEqual(self.s2.id, 9)
        self.assertEqual(self.s2.width, 5)
        self.assertEqual(self.s2.height, 5)
        self.assertEqual(self.s2.x, 10)
        self.assertEqual(self.s2.y, 5)

        self.assertEqual(self.s3.id, 10)
        self.assertEqual(self.s3.width, 50)
        self.assertEqual(self.s3.height, 50)
        self.assertEqual(self.s3.x, 0)
        self.assertEqual(self.s3.y, 0)

    # Testing errors for __init__

    def testSquareInitErrors(self):
        with self.assertRaises(TypeError):
            s4 = Square()
            s4 = Square("String")
            s5 = Square(5, "String")
            s5 = Square(5, 6, "String")
            s5 = Square(5, 6, 7, "String")

        with self.assertRaises(ValueError):
            s6 = Square(0, id=0)
            s6 = Square(-1, id=0)
            s6 = Square(1, 0, id=0)

    # Testing square setter w/ errors

    def testSquareSetter(self):
        S = Square(2)
        S.id = 69
        self.assertEqual(S.id, 69)
        S.width = 420
        self.assertEqual(S.width, 420)
        S.height = 350
        self.assertEqual(S.height, 350)
        S.x = 10
        self.assertEqual(S.x, 10)
        S.y = 15
        self.assertEqual(S.y, 15)

        with self.assertRaises(TypeError):
            S.size = "string"
            S.size = True
            S.size = {1, 2, 3}
            S.size = (1, 2, 3)
            S.size = [1, 2, 3]

        with self.assertRaises(ValueError):
            S.size = -1
            S.size = 0

    # Testing update with ARGS

    def testUpdateArgs(self):
        R = Square(2, 2, id=0)
        self.assertEqual(R.id, 0)
        self.assertEqual(R.width, 2)
        self.assertEqual(R.height, 2)
        self.assertEqual(R.x, 2)
        self.assertEqual(R.y, 0)

        R.update(69)
        self.assertEqual(R.id, 69)
        self.assertEqual(R.width, 2)
        self.assertEqual(R.height, 2)
        self.assertEqual(R.x, 2)
        self.assertEqual(R.y, 0)

        R.update(350, 420)
        self.assertEqual(R.id, 350)
        self.assertEqual(R.width, 420)
        self.assertEqual(R.height, 420)
        self.assertEqual(R.x, 2)
        self.assertEqual(R.y, 0)

        R.update(69, 350, 420)
        self.assertEqual(R.id, 69)
        self.assertEqual(R.width, 350)
        self.assertEqual(R.height, 350)
        self.assertEqual(R.x, 420)
        self.assertEqual(R.y, 0)

        R.update(1, 2, 3, 4)
        self.assertEqual(R.id, 1)
        self.assertEqual(R.width, 2)
        self.assertEqual(R.height, 2)
        self.assertEqual(R.x, 3)
        self.assertEqual(R.y, 4)

    # Testing update with KWARGS

    def testUpdateKWARGS(self):
        R = Square(2, 2, id=0)
        self.assertEqual(R.id, 0)
        self.assertEqual(R.width, 2)
        self.assertEqual(R.height, 2)
        self.assertEqual(R.x, 2)
        self.assertEqual(R.y, 0)

        R.update(width=69, id=420)
        self.assertEqual(R.id, 420)
        self.assertEqual(R.width, 69)
        self.assertEqual(R.height, 2)
        self.assertEqual(R.x, 2)
        self.assertEqual(R.y, 0)

        R.update(x=5, width=350, y=10, id=69)
        self.assertEqual(R.id, 69)
        self.assertEqual(R.width, 350)
        self.assertEqual(R.height, 2)
        self.assertEqual(R.x, 5)
        self.assertEqual(R.y, 10)

    # Testing create from class Base within square

    def testCreate(self):
        S = Square(5, 4, 3, 2)
        S_dic = S.to_dictionary()
        S2 = Square.create(**S_dic)
        self.assertEqual(S2.id, 2)
        self.assertEqual(S2.width, 5)
        self.assertEqual(S2.height, 5)
        self.assertEqual(S2.x, 4)
        self.assertEqual(S2.y, 3)

    # Testing pep8 on the file

    def testPep8(self):
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(
            ['models/base.py', 'models/rectangle.py', 'models/square.py'])

        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")
