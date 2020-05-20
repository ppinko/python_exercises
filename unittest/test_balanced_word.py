import unittest
from balanced_word import balanced

class TestBalance(unittest.TestCase):

    def test_value(self):
        self.assertTrue(balanced("zips"))
        self.assertFalse(balanced("brake"))

    def test_type(self):
        self.assertRaises(TypeError, balanced, 1)
        self.assertRaises(TypeError, balanced, (1, 1))
        self.assertRaises(TypeError, balanced, [1, 2])
        self.assertRaises(TypeError, balanced, {1:2, 2:3})

    def test_string(self):
        self.assertRaises(ValueError, balanced, "Herborn")
        self.assertRaises(ValueError, balanced, "123asd")
        self.assertRaises(ValueError, balanced, "herb orn")
        self.assertRaises(ValueError, balanced, "as^da")
