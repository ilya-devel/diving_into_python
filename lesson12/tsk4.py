"""
Доработайте класс прямоугольник из прошлых семинаров.
Добавьте возможность изменять длину и ширину
прямоугольника и встройте контроль недопустимых значений
(отрицательных).
Используйте декораторы свойств.
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

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, value):
        if value > 0:
            self.__length = value
        else:
            print("Результат получается отрицательный, операция не проведена")

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if value > 0:
            self.__width = value
        else:
            print("Результат получается отрицательный, операция не проведена")


if __name__ == '__main__':
    tmp = Rectangle(4, 5)
    print(tmp.length)
    tmp.length = -10
    tmp.length = 5
    print(tmp.length)
