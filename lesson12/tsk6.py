"""
Изменяем класс прямоугольника.
Заменяем пару декораторов проверяющих длину и ширину
на дескриптор с валидацией размера.
"""


class Value:
    def __init__(self, value: int = None):
        self.value = value

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)

    def __delete__(self, instance):
        raise AttributeError(f"Свойство {self.param_name} нельзя удалять")

    def validate(self, value):
        if not isinstance(value, int):
            raise TypeError(f"Значение {value} должно быть целым числом")
        if value <= 0:
            raise ValueError(f"Значение {value} должно быть больше 0")


class Rectangle:
    length = Value()
    width = Value()

    def __init__(self, length=None, width=None):
        # if length is None and width is None:
        #     length, width = 1, 1
        # elif width is None or length is None:
        #     width = length if width is None else width
        #     length = width if length is None else length
        self.length = length
        self.width = width

    def get_area(self):
        return self.width * self.length

    def get_perimeter(self):
        return self.width * 2 + self.length * 2

    def __str__(self):
        return f"Прямоугольник со сторонами {self.width} X {self.length}"


if __name__ == '__main__':
    tmp = Rectangle(1, 10)
    print(tmp)
    tmp.length = 10
    print(tmp.__dict__)
    pass
