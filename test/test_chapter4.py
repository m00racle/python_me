import os 
import sys
tested_path = os.path.normpath(os.path.dirname(__file__) + "/../src/6-006_python/chap04")
sys.path.append(tested_path)

import unittest
from chapter4 import find_max_cross_subarray as cross, find_max_subarray as subs
from chapter4 import brute_max_subarray as brute
from chapter4 import iterative_max_subarray as iter

class TestChap04(unittest.TestCase):
    """
    test case for chap04
    """

    def setUp(self) -> None:
        self.negA = [-13, -13, -25, -20, -3, -16, -23, -18, -20, -17, -12, -5, -22, -15, -4, -7]
        self.testA = testA = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
        return super().setUp()

    def tearDown(self) -> None:
        self.negA = []
        self.testA = []
        return super().tearDown()
    
    def test_find_cross_max(self):
        """
        test find cross sub-array for max sum value
        """
        # prepare
        crossA = [-1, -3, 12, -6, 10, -3, 7, 3, -12, 8, -1]
        # assert
        self.assertEqual(cross(crossA, 1, len(crossA)//2, len(crossA)), (3, 8, 23))
        
    def test_find_max_subarray(self):
        """
        test finding maximum sub-array
        """
        # assert (8, 11, 43)
        self.assertEqual(subs(self.testA, 1, len(self.testA)), (8, 11, 43))
    
    def test_find_max_subarray_negA(self):
        """
        test finding the max on array full of negative numbers
        should return single largest number in the array
        """
        # assert (5, 5, -3)
        self.assertEqual(subs(self.testA, 1, len(self.testA)), (5, 5, -3))
    
    def test_brute_force_find_max_subarray(self):
        """
        test if the brute force find consistent result
        """
        self.assertEqual(brute(self.testA, 1, len(self.testA)), (8, 11, 43))
    
    def test_brute_find_max_sub_array(self):
        """
        test the brute force for all negative array
        """
        self.assertEqual(brute(self.negA, 1, len(self.negA)), (5, 5, -3))
    
    def test_iterative_finding_max_positive_sub_array(self):
        """
        testing iterative finding positive sub_array
        """
        self.assertEqual(iter(self.testA, 1, len(self.testA)), (8, 11, 43))
    

if __name__ == "__main__":
    unittest.main(verbosity=2)
