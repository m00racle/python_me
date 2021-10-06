import os, sys
tested_path = os.path.normpath(os.path.dirname(__file__) + "/../src/6-006_python/chap04")
sys.path.append(tested_path)

import unittest
from matrix import matrix_product as mprod

class TestMatrix4(unittest.TestCase):
    """
    tests for matrix.py
    """

    def setUp(self) -> None:
        return super().setUp()

    def tearDown(self) -> None:
        return super().tearDown()

    def test_normal_matrix_multiplication(self):
        """
        test normal matrix of shape (2 x 3) to (3 x 2)
        """
        # prepare
        A = [[2,1,3], [4,5,6]]
        B = [[3,1], [1,2], [1,1]]
        C = [[10, 7], [23, 20]]
        # asssert
        self.assertEqual(mprod(A,B), C)
        