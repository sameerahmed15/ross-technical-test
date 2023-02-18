import unittest
import sys
sys.path.insert(1, './src')
import src.partial_flip_sort as partial_flip_sort

class TestFlipSort(unittest.TestCase):

    def test_partial_flip(self):
        self.assertEqual(partial_flip_sort.partial_flip([3,2,4,1], 4), [1,4,2,3])
        self.assertEqual(partial_flip_sort.partial_flip([3,2,4,1], 3), [4,2,3,1])

    def test_sorting(self):
        self.assertEqual(partial_flip_sort.sorting([3,2,4,1]), [3,4,2,3,1,2])
        self.assertEqual(partial_flip_sort.sorting([3,2,4,1,7,5,6]), [5,7,1,6,5,5,2,4,1,3,2,2])


if __name__ == '__main__':
    unittest.main()