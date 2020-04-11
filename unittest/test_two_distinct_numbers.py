import unittest
from two_distinct_numbers import return_unique

class TestDistinctNumbers(unittest.TestCase):

    def test_result(self):
        self.assertListEqual(return_unique([1, 9, 8, 8, 7, 6, 1, 6]), [9, 7])
        self.assertListEqual(return_unique([5, 5, 2, 4, 4, 4, 9, 9, 9, 1]), [2, 1])
        self.assertListEqual(return_unique([9, 5, 6, 8, 7, 7, 1, 1, 1, 1, 1, 9, 8]), [5, 6])

    def test_main_type(self):
        self.assertRaises(TypeError, return_unique, "city")
        self.assertRaises(TypeError, return_unique, 1)
        self.assertRaises(TypeError, return_unique, (1, 2, 3))
        self.assertRaises(TypeError, return_unique, {1:2, 2:3})

    def test_subtype(self):
        self.assertRaises(TypeError, return_unique, ['a', 'b'])
        self.assertRaises(TypeError, return_unique, [1.5, 1, 2])
        self.assertRaises(TypeError, return_unique, [(1,), (2, 3)])
