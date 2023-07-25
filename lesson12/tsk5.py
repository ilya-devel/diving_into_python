"""
Доработаем прямоугольник и добавим экономию памяти
для хранения свойств экземпляра без словаря __dict__.
"""
from pprint import pprint

from lesson12.tsk4 import Rectangle


class NewRectangle(Rectangle):
    __slots__ = ['__width', '__length']


if __name__ == '__main__':
    tmp = NewRectangle(4, 5)
    pprint(NewRectangle.__dict__)
    print()
    pprint(tmp.__dict__)
