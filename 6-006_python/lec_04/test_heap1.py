import unittest
import heap1
heap = heap1

class TestHeap(unittest.TestCase):

    def test_parent(self):
        self.assertEqual(heap.parent(5),2,msg='when child i is 5 should return 2 not 2.5')
        self.assertEqual(heap.parent(4), 2, 'should equal 2')

    def test_left(self):
        # the left should be returning 2 times the current index
        self.assertEqual(heap.left(3), 6, 'should return 6')
    
    def test_right(self):
        # the right should return 2 times index plus 1
        self.assertEqual(heap.right(3), 7, 'should return 7')

    def test_maxHeapify(self):
        # prepare the A array:
        A = [16, 4, 10, 14, 7, 9, 3, 2, 8, 1]
        Alast = heap1.maxHeapify(A, 2)
        self.assertEqual(Alast, [16, 14, 10, 8, 7, 9, 3, 2, 4, 1])

if __name__ == '__main__':
    unittest.main(verbosity=2)
