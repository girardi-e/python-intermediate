import unittest
from divisible import divisible_by


class DivisibleTestCase(unittest.TestCase):

    def test_divisible_by(self):
        self.assertTrue(divisible_by(10, 5))
        self.assertFalse(divisible_by(3, 2))


if __name__ == "__main__":
    unittest.main()
