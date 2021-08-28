import os
import sys
tested_path = os.path.normpath(os.path.dirname(__file__) + "/../src/6-006_python/rec_sort")
sys.path.append(tested_path)

import unittest
from sorting import insertionSort

class TestSorting(unittest.TestCase):
    """
    this is test for the sorting.py
    """
    def setUp(self):
        self.initA = [31,41,59,26,41,58,1,8,15,22]
        self.increasing = [1,8,15,22,26,31,41,41,58,59]
        self.decreasing = [59,58,41,41,31,26,22,15,8,1]

    def test_insertion_increasing_sort(self):
        """
        test the whole insertion sort
        """
        self.assertEqual(insertionSort(self.initA), self.increasing)

    def test_insertion_decreasing_sort(self):
        """
        test the whole isertion sort for decreasing order
        """
        self.assertEqual(insertionSort(self.initA, False), self.decreasing)

if __name__ == '__main__':
    unittest.main(verbosity=2)