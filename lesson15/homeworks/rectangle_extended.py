"""
Возьмите 1-3 задачи из тех, что были на прошлых
семинарах или в домашних заданиях. Напишите к ним
классы исключения с выводом подробной информации.
Поднимайте исключения внутри основного кода. Например
нельзя создавать прямоугольник со сторонами
отрицательной длины.
"""


class ArgumentNotFound(TypeError):
    def __init__(self, value=None):
        self.value = value

    def __str__(self):
        return f"Не было передано ни одного аргумента. {self.value if self.value is not None else ''}"


class NonPositiveError(TypeError):
    def __init__(self, value=None):
        self.value = value

    def __str__(self):
        return f"Значене не может быть отрицательным. {self.value if self.value is not None else ''}"


class NotZeroError(TypeError):
    def __init__(self, value=None):
        self.value = value

    def __str__(self):
        return f"Значене не может быть 0. {self.value if self.value is not None else ''}"


class Rectangle:
    def __init__(self, length=None, width=None):
        self.is_valid(length, width)
        if width is None or length is None:
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

    def get_width(self):
        return self.__width

    def get_length(self):
        return self.__length

    @staticmethod
    def is_valid(length, width):
        if length is None and width is None:
            raise ArgumentNotFound(f"{length = }, {width = }")
        if (length is not None and length < 0) or (width is not None and width < 0):
            raise NonPositiveError(f"{f'{length = }' if length < 0 else f'{width = }'}")
        if (length is not None and length == 0) or (width is not None and width == 0):
            raise NotZeroError(f"{f'{length = }' if length == 0 else f'{width = }'}")


if __name__ == '__main__':
    args = [
        {'length': None, 'width': None},
        {'length': -1, 'width': 3},
        {'length': 1, 'width': -3},
        {'length': 1, 'width': 0},
        {'length': 0, 'width': 3},
        {'length': 3, 'width': 5},
        {'length': 5, 'width': None},
        {'length': None, 'width': 6},
    ]
    lst = []
    for arg in args:
        try:
            lst.append(Rectangle(**arg))
        except (ArgumentNotFound, NonPositiveError, NotZeroError) as err:

            print(err)
    print()
    for rectangle in lst:
        print(f"{rectangle} имеет площадь {rectangle.get_area()}")
        print(f"{rectangle} имеет периметр {rectangle.get_perimeter()}")
