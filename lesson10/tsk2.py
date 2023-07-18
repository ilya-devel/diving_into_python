"""
Создайте класс прямоугольник.
Класс должен принимать длину и ширину при создании
экземпляра.
У класса должно быть два метода, возвращающие периметр
и площадь.
Если при создании экземпляра передаётся только одна
сторона, считаем что у нас квадрат.
"""


class Rectangle:
    def __init__(self, length=None, width=None):
        if length is None and width is None:
            length, width = 1, 1
        elif width is None or length is None:
            width = length if width is None else width
            length = width if length is None else length
        self.__length = length
        self.__width = width

    def get_area(self):
        return self.__width * self.__length

    def get_perimeter(self):
        return self.__width * 2 + self.__length * 2

    def __str__(self):
        return f"Прямоугольник со сторонами {self.__width} X {self.__length}"


if __name__ == '__main__':
    lst = [Rectangle(), Rectangle(1, 2), Rectangle(3), Rectangle(length=4), Rectangle(width=5)]
    for rectangle in lst:
        print(f"{rectangle} имеет площадь {rectangle.get_area()}")
        print(f"{rectangle} имеет периметр {rectangle.get_perimeter()}")
