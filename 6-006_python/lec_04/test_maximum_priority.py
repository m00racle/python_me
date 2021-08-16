import unittest
import maximum_priority

prior = maximum_priority

# this is the test python file for maximum_priority.py

class TestMaximumPriority(unittest.TestCase):

    def setUp(self):
        # prepare 
        self.A = [16,14,10,8,7,9,3,2,4,1]

    def test_heap_maximum(self):
        # assert return A[1]
        self.assertEqual(prior.heapMax(self.A),16)
    
    def test_heap_extract_value_error(self):
        with self.assertRaises(ValueError):
            prior.heapExtractMax(self.A, 0)
    
    def test_heap_extract_max_return_max_element(self):
        # assert heapExtraxtMax(A. len(A)) to be 16 as the max heap (root of the whole heap)
        self.assertEqual(prior.heapExtractMax(self.A, len(self.A)), 16)

if __name__ == '__main__':
    unittest.main(verbosity=2)
