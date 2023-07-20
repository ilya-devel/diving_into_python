"""
Дорабатываем класс прямоугольник из прошлого семинара.
Добавьте возможность сложения и вычитания.
При этом должен создаваться новый экземпляр
прямоугольника.
Складываем и вычитаем периметры, а не длинну и ширину.
При вычитании не допускайте отрицательных значений.
"""

from lesson10.tsk2 import Rectangle


class RectangleExtended(Rectangle):
    def __add__(self, other):
        perimetr = self.get_perimeter() + other.get_perimeter()
        return RectangleExtended(perimetr / 4)

    def __sub__(self, other):
        perimetr = self.get_perimeter() - other.get_perimeter()
        return RectangleExtended(abs(perimetr) / 4)


if __name__ == '__main__':
    rect1 = RectangleExtended(5)
    rect2 = RectangleExtended(4, 2)
    rect3 = rect2 - rect1
    print(rect3)
