from logging import setLoggerClass
import os
import sys
from unittest import result
tested_path = os.path.normpath(os.path.dirname(__file__) + "/../src/modules")
sys.path.append(tested_path)

import unittest
import inverse

class TestInverse(unittest.TestCase):
    """
    test the library inverse.py
    """

    def setUp(self) -> None:
        self.baseN = 223
        self.baseA = 99
        self.result = inverse.inverseOf(self.baseA, self.baseN)
        return super().setUp()
    
    def tearDown(self) -> None:
        return super().tearDown()

    def test_non_co_prime_invoke_error(self):
        """
        Test if the mod basis and the number is not a co prime 
        The lib should return error (invole error)
        """
        with self.assertRaises(ValueError):
            inverse.inverseOf(175,49)

    def test_inverse_value_must_be_positive(self):
        """
        the inverse must be postive to be useful
        """
        # assert
        self.assertTrue(self.result > 0, "failed: result is negative")

    
    def test_inverse_should_result_1_in_mod_multiplied(self):
        """
        the inverse when multiplied to the smaller parameter should result 1
        when in the mod of bigger parameter.
        """
        # assert
        self.assertEqual((self.result * self.baseA) % self.baseN, 1, "failed: result is not an inverse")
