import unittest
# Import the code to be tested
from multiply import multiply


# TestCase class must subclass unittest.TestCase
class TestMultiply(unittest.TestCase):

    # Names of test functions must begin with test_
    def test_multiply(self):
        test_x = 5
        test_y = 10
        self.assertEqual(multiply(test_x, test_y), 50, "Should be 50.")

# running unit test
if __name__ == "__main__":
    unittest.main()

# another way to run unit tests: python -m unittest filename -v
