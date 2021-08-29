import os
import sys

tested_dir = os.path.normpath(os.path.dirname(__file__) + "/../src/modules")
print(tested_dir)
sys.path.append(tested_dir)

import unittest
from idx import idx

class testIdxModule(unittest.TestCase):
    """
    this is the test to idx scenarios and functions.
    """

    def test_normal_idx_conversion(self):
        """
        test the indexing conversion using the common integer
        """
        self.assertEqual(idx(4), 3)
    
    def test_converting_number_1(self):
        """
        conversion of the limit number 1 should not invoke errors
        """
        self.assertEqual(idx(1), 0)

    def test_converting_0_invoke_error(self):
        """
        conversion i = 0 should invoke ValueError
        """
        with self.assertRaises(ValueError):
            idx(0)
        
    def test_less_than_one_raise_error(self):
        """
        input less than 1 should raise value error
        """
        with self.assertRaises(ValueError):
            idx(0.9)
    
    

if __name__ == '__main__':
    unittest.main(verbosity=2)