import unittest
from lesson12.tsk3 import FactorialGenerate


class TestFactorialGenerate(unittest.TestCase):

    def test_without_arguments(self):
        self.assertRaises(Exception, FactorialGenerate)

    def test_with_four_arguments(self):
        self.assertEqual([i for i in FactorialGenerate(1, 5, 1, 5)], [1, 2, 6, 24, 120])

    def test_with_three_arguments(self):
        self.assertEqual([i for i in FactorialGenerate(1, 5, 1)], [1, 2, 6, 24, 120])

    def test_with_two_arguments(self):
        self.assertEqual([i for i in FactorialGenerate(1, 5)], [1, 2, 6, 24, 120])

    def test_with_one_arguments(self):
        self.assertEqual([i for i in FactorialGenerate(5)], [1, 2, 6, 24, 120])


if __name__ == '__main__':
    unittest.main(verbosity=True)
