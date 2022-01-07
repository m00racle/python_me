from logging import setLoggerClass
import os
import sys
from unittest import result
tested_path = os.path.normpath(os.path.dirname(__file__) + "/../src/modules")
sys.path.append(tested_path)

import unittest
import pulverizer

class TestPulverizer(unittest.TestCase):
    """
    test case for pulverizer
    """
    def setUp(self) -> None:
        return super().setUp()
    
    def tearDown(self) -> None:
        return super().tearDown()
    
    def test_divisor_as_gcd(self):
        """
        the scenario is if the divisor is the gcd in the second parameter.
        """
        # setup
        result = pulverizer.gcd(400,20)
        # assert
        self.assertEqual(result.value, 20, "value is not match the gcd")
        self.assertEqual([result.s, result.t], [0,1], "the s and t coefficients is not correct")
    
    def test_divisior_as_first_param_gcd(self):
        """
        the scenario is for the divisor as first param
        """
        # set
        result = pulverizer.gcd(50, 400)
        # assert
        self.assertEqual([result.value, result.s, result.t], [50, 1, 0], "the result list order is incorrect")

    def test_longer_remainder_gcd(self):
        """
        the scenario is for the gcd of two numbers which directly product of two primes.
        """
        result = pulverizer.gcd(221, 91)
        # assert
        self.assertEqual([result.value, result.s, result.t], [13, -2, 5], "longer gcd linear comb incorrect")
    
    def test_longer_remainder_gcd_reversed_params(self):
        """
        test the scenario of product of primes gcd but the parameters are on reversed order
        """
        result = pulverizer.gcd(91, 221)
        # assert
        self.assertEqual([result.value, result.s, result.t], [13, 5, -2], "reversed order incorrect")

    