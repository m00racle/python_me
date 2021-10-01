import os 
import sys
tested_path = os.path.normpath(os.path.dirname(__file__) + "/../src/6-006_python/chap04")
sys.path.append(tested_path)

import unittest
from chapter4 import find_max_cross_subarray as cross, find_max_subarray as subs

class TestChap04(unittest.TestCase):
    """
    test case for chap04
    """

    def setUp(self) -> None:
        return super().setUp()

    def tearDown(self) -> None:
        return super().tearDown()
    
    def test_find_cross_max(self):
        """
        test find cross sub-array for max sum value
        """
        # prepare
        crossA = [-1, -3, 12, -6, 10, -3, 7, 3, -12, 8, -1]
        # assert
        self.assertEqual(cross(crossA, 0, len(crossA)//2, len(crossA)), (3, 8, 23))
        
    def test_find_max_subarray(self):
        """
        test finding maximum sub-array
        """
        # prepare
        testA = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
        # assert (7, 10, 43)
        self.assertEqual(subs(testA, 1, len(testA)), (8, 11, 43))
    
if __name__ == "__main__":
    unittest.main(verbosity=2)
