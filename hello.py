# test_hello_world.py

import unittest
from hello_world import greet

class TestHelloWorld(unittest.TestCase):
    def test_greet(self):
        """
        Test that the greet function returns 'Hello, World!'
        """
        self.assertEqual(greet(), "Hello, World!")

if __name__ == "__main__":
    unittest.main()
