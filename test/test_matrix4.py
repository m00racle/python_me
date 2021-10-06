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

    def test_mismatch_matrix_A_and_B(self):
        """
        test if the matrix B row is insufficient
        """
        # prepare
        A = [[2,1,3], [4,5,6]]
        B = [[3,1], [1,1]]
        # assert raise exception
        with self.assertRaises(Exception):
            mprod(A,B)
    
    def test_mismatch_matrixA(self):
        """
        test raise exception mismatch matrix A
        """
        # prepare
        A = [[2,1,3], [4,5]]
        B = [[3,1], [1,2], [1,1]]
        # assertRaiseException
        with self.assertRaises(Exception):
            mprod(A,B)

    def test_mismatch_matrix_B_non_symetric(self):
        """
        test raise exception mismatch matrix B
        """
        # prepare
        A = [[2,1,3], [4,5,6]]
        B = [[3,1], [1], [1,1]]
        # assert raise exception
        with self.assertRaises(Exception):
            mprod(A,B)
    
