"""
This module performs unit testing of square function
"""

import unittest

from square import squareOfNum

class TestSquareFunction(unittest.TestCase):
    def test_square(self):
        self.assertEqual(squareOfNum(4), 16)

if __name__ == '__main__':
    unittest.main()
