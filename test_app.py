# test_app.py
import unittest
from app import *

class TestApp(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()
