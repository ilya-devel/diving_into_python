"""
Создайте класс окружность.
Класс должен принимать радиус окружности при создании
экземпляра.
У класса должно быть два метода, возвращающие длину
окружности и её площадь.
"""
import math


class Circle:
    def __init__(self, radius=1):
        self.__radius = radius

    def get_length(self):
        return 2 * math.pi * self.__radius

    def get_area(self):
        return math.pi * self.__radius ** 2

    def get_radius(self):
        return self.__radius


if __name__ == '__main__':
    lst = [Circle(), Circle(5)]
    for circle in lst:
        print(f"Длина окружности с радиусом {circle.get_radius()} равна: {circle.get_length()}")
        print(f"Площадь окружности с радиусом {circle.get_radius()} равна: {circle.get_area()}")
