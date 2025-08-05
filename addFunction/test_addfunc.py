"""
The module contains test class for the addfunc.py file
"""

import unittest

from addfunc import addition
class TestAddFunction(unittest.TestCase):
    def test_summation(self):
        self.assertEqual(addition(10,10),20)

if __name__ == '__main__':
    unittest.main()
