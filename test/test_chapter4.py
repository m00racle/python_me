import os 
import sys
tested_path = os.path.normpath(os.path.dirname(__file__) + "/../src/6-006_python/chap04")
sys.path.append(tested_path)

import unittest
from chapter4 import find_max_cross_subarray as cross

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
        crossA = [-1, -3, 12, -6, 10, -3, 7, 3, -12, 8]
        