"""

To run test in terminal type:
    python3 -m unittest test_filname
    (-m -> run library module as a script)

    Example result:
    [devlx@localhost unittest]$ python3 -m unittest test_circle_area
    .
    ----------------------------------------------------------------------
    Ran 1 test in 0.000s

    OK
    [devlx@localhost unittest]$

    Looking for help on the function (example):
        import unittest
        help(unittest.TestCase.assertSetEqual)

"""

# Crucial to import 'unitttest'

import unittest 
from circle_area import circle_area
from math import pi

"""
testing class should be derived from unittest.TestCase
"""

class TestCircle(unittest.TestCase):
    """
    Test function must statu with word 'test', otherwise it won't be detected
    """
    def test_area(self):
        # Test area when radius >= 0
        # assertAlmostEqual good for floats - precision 7 digits
        self.assertAlmostEqual(circle_area(1), pi)
        self.assertAlmostEqual(circle_area(0), 0)
        self.assertAlmostEqual(circle_area(2), pi*2**2)

    def test_values(self):
        # Make sure ValueErrors are raised when necessary
        self.assertRaises(ValueError, circle_area, -2)

    def test_types(self):
        # Make sure ValueErrors are raised when necessary
        self.assertRaises(TypeError, circle_area, 3+5j)
        self.assertRaises(TypeError, circle_area, True)
        self.assertRaises(TypeError, circle_area, "radius")
        
