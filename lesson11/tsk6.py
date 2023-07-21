"""
Доработайте прошлую задачу.
Добавьте сравнение прямоугольников по площади
Должны работать все шесть операций сравнения
"""

from tsk5 import RectangleExtended


class RectangleExtendedSecond(RectangleExtended):
    """
    Дополнительное расширение класса RectangleExtended, добавляющий возможность сравнения двух прямоугольников по площади
    """

    def __eq__(self, o: object) -> bool:
        return self.get_area() == o.get_area()

    def __ne__(self, o: object) -> bool:
        return self.get_area() != o.get_area()

    def __gt__(self, o: object) -> bool:
        return self.get_area() > o.get_area()

    def __ge__(self, o: object) -> bool:
        return self.get_area() <= o.get_area()

    def __lt__(self, o: object) -> bool:
        return self.get_area() < o.get_area()

    def __le__(self, o: object) -> bool:
        return self.get_area() >= o.get_area()


if __name__ == '__main__':
    print(RectangleExtendedSecond() == RectangleExtendedSecond())
    print(RectangleExtendedSecond() != RectangleExtendedSecond())
    print(RectangleExtendedSecond() >= RectangleExtendedSecond())
    print(RectangleExtendedSecond() <= RectangleExtendedSecond())
    print(RectangleExtendedSecond() > RectangleExtendedSecond())
    print(RectangleExtendedSecond() < RectangleExtendedSecond())
    help(RectangleExtendedSecond)
    print(RectangleExtendedSecond())
