import os
import sys
tested_path = os.path.normpath(os.path.dirname(__file__) + "/../src/6-006_python/rec_sort")
sys.path.append(tested_path)

import unittest
from sorting import insertionSort, mergeSort, listSeparator, merge

class TestSorting(unittest.TestCase):
    """
    this is test for the sorting.py
    """
    def setUp(self) -> None:
        self.initA = [31,41,59,26,41,58,1,8,15,22,75]
        self.increasing = [1,8,15,22,26,31,41,41,58,59,75]
        self.decreasing = [75,59,58,41,41,31,26,22,15,8,1]
        return super().setUp()

    def tearDown(self) -> None:
        self.initA = None
        self.increasing = None
        self.decreasing = None
        return super().tearDown()

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

    def test_merge_sort_ascending(self):
        """
        test the merge sort in ascending order
        """
        self.assertEqual(mergeSort(self.initA), self.increasing)

    def test_merge_sort_descending(self):
        """
        test the merge sort in descending order
        """
        self.assertEqual(mergeSort(self.initA, False), self.decreasing)

    def test_merge_ascending(self):
        (lo, hi) = ([5,9,12], [9, 11, 13, 15])
        self.assertEqual(merge(lo,hi,True), [5,9,9,11,12,13,15])
    
    def test_merge_descending(self):
        (lo, hi) = ([12,9,5], [15,13,11,9])
        self.assertEqual(merge(lo,hi,False), [15,13,12,11,9,9,5])

if __name__ == '__main__':
    unittest.main(verbosity=2)