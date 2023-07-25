"""
Создайте класс-функцию, который считает факториал числа при
вызове экземпляра.
Экземпляр должен запоминать последние k значений.
Параметр k передаётся при создании экземпляра.
Добавьте метод для просмотра ранее вызываемых значений и
их факториалов
"""
from collections import defaultdict


class Factorial:
    def __init__(self):
        self._storage = defaultdict(int)

    def __call__(self, value, *args, **kwargs):
        if f'!{value}' in self._storage.keys():
            return self._storage[f'!{value}']
        res = 1
        for x in range(1, value + 1):
            res *= x
        self._storage[f'!{value}'] = res
        return res

    def get_all_result(self):
        return self._storage


if __name__ == '__main__':
    tmp = Factorial()
    print(tmp(7))
    print(tmp(5))
    print(tmp(1000))
    print(tmp.get_all_result())
