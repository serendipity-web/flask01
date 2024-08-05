import unittest
from easy_way import add, subtract, multiply, divide


class TestBasicMath(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(1, 2), 3)

    def test_subtract(self):
        self.assertEqual(subtract(1, 2), -1)

    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertRaises(ValueError, divide, 10, 0)


if __name__ == '__main__':
    unittest.main()
