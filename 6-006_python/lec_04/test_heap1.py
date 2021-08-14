import unittest
import heap1

class TestHeap(unittest.TestCase):

    def test_parent(self):
        self.assertEqual(heap1.parent(5),2,msg='when child i is 5 should return 2 not 2.5')
        self.assertEqual(heap1.parent(4), 2, 'should equal 2')

    def test_left(self):
        # the left should be returning 2 times the current index
        self.assertEqual(heap1.left(3), 6, 'should return 6')
    
    def test_right(self):
        # the right should return 2 times index plus 1
        self.assertEqual(heap1.right(3), 7, 'should return 7')

    def test_maxHeapify(self):
        # prepare the A array:
        A = [16, 4, 10, 14, 7, 9, 3, 2, 8, 1]
        Alast = heap1.maxHeapify(A, 2)
        self.assertEqual(Alast, [16, 14, 10, 8, 7, 9, 3, 2, 4, 1])

    def test_indexing(self):
        self.assertEqual(heap1.ind(2), 1, "should be index 1 as i key is 2")
        with self.assertRaises(ValueError):
            heap1.ind(0)
    
    def test_minHeapify(self):
        # this is the reversed version of the maxHeapify test
        A = [1,8,2,3,9,7,14,10,4,16]
        Amin = heap1.minHeapify(A, 2)
        self.assertEqual(Amin, [1,3,2,4,9,7,14,10,8,16])

    def test_maxLoopHeapify(self):
        # prepare the A array:
        A = [16, 4, 10, 14, 7, 9, 3, 2, 8, 1]
        Alast = heap1.maxLoopHeapify(A, 2)
        self.assertEqual(Alast, [16, 14, 10, 8, 7, 9, 3, 2, 4, 1])

    def test_break_mid_maxHeapify(self):
        # prepare the A array:
        A = [16, 11, 15, 14, 7, 9, 3, 2, 8, 1]
        Alast = heap1.maxHeapify(A, 2)
        self.assertEqual(Alast, [16, 14, 15, 11, 7, 9, 3, 2, 8, 1])

    def test_break_mid_maxLoopHeapify(self):
        # prepare the A array:
        A = [16, 11, 15, 14, 7, 9, 3, 2, 8, 1]
        Alast = heap1.maxLoopHeapify(A, 2)
        self.assertEqual(Alast, [16, 14, 15, 11, 7, 9, 3, 2, 8, 1])

    def test_build_maxHeapify(self):
        # prepare :
        A = [4,1,3,2,16,9,10,14,8,7]
        # action
        Amax = heap1.buildMaxHeap(A)
        # assert
        self.assertEqual(Amax, [16,14,10,8,7,9,3,2,4,1])

if __name__ == '__main__':
    unittest.main(verbosity=2)
