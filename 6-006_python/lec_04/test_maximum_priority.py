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

    def test_increase_key(self):
        # assert increases key that substitute element number 9
        # the value in element number 9 is 4
        # that value is substituted with the key = 15
        # the process will increase the key at element number 2 below root 
        # other elements passed by the key will be shofted to child position
        self.assertEqual(prior.heapIncreaseKey(self.A, 9, 15), [16,15,10,14,7,9,3,2,8,1])

    def test_value_error_increase_key(self):
        # test when the key substituting the element (index 5) value
        # but the key = 6, is smaller compared to the current key element=7
        # it should raise value error
        with self.assertRaises(ValueError):
            prior.heapIncreaseKey(self.A, 5, 6)

    

if __name__ == '__main__':
    unittest.main(verbosity=2)
