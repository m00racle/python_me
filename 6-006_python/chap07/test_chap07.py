import unittest
import chap07

class TestChap07(unittest.TestCase):
    # this is the test for the  chap07.py

    def setUp(self):
        self.A = [2,8,7,1,3,5,6,4]

    def test_partition(self):
        # action 
        q, partA = chap07.partition(self.A, 1, len(self.A))
        # assert 1 assert the q
        self.assertEqual(q, 4, 'the q returned should be 4')
        self.assertEqual(partA, [2,1,3,4,7,5,6,8])
    
    def test_quicksort(self):
        # action
        sortA = chap07.quicksort(self.A, 1, len(self.A))
        # assert
        self.assertEqual(sortA, [1,2,3,4,5,6,7,8])


if __name__ == '__main__':
    unittest.main(verbosity=2)
