"""
📌На семинарах по ООП был создан класс прямоугольник
хранящий длину и ширину, а также вычисляющую периметр,
площадь и позволяющий складывать и вычитать
прямоугольники беря за основу периметр.
📌Напишите 3-7 тестов unittest для данного класса.
"""
import math

from lesson10.tsk1 import Circle
import unittest


class TestCircle(unittest.TestCase):
    def setUp(self):
        self.circle1 = Circle(10)
        self.circle2 = Circle(20)
        self.circle3 = Circle(50)
        self.circle4 = Circle(100)

    def test_length_10(self):
        self.assertEqual(2 * math.pi * 10, self.circle1.get_length())

    def test_length_20(self):
        self.assertEqual(2 * math.pi * 20, self.circle2.get_length())

    def test_length_50(self):
        self.assertEqual(2 * math.pi * 50, self.circle3.get_length())

    def test_length_100(self):
        self.assertEqual(2 * math.pi * 100, self.circle4.get_length())


if __name__ == '__main__':
    unittest.main(verbosity=2)
