import unittest

import partialflipsort

class TestFlipSort(unittest.TestCase):

    def test_partial_flip(self):
        self.assertEqual(partialflipsort.partial_flip([3,2,4,1], 4), [1,4,2,3])
        self.assertEqual(partialflipsort.partial_flip([3,2,4,1], 3), [4,2,3,1])

    def test_sorting(self):
        self.assertEqual(partialflipsort.sorting([3,2,4,1]), [3,4,2,3,1,2])
        self.assertEqual(partialflipsort.sorting([3,2,4,1,7,5,6]), [5,7,1,6,5,5,2,4,1,3,2,2])


if __name__ == '__main__':
    unittest.main()