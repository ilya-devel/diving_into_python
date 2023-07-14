"""
Дорабатываем задачу 1.
Превратите внешнюю функцию в декоратор.
Он должен проверять входят ли переданные в функциюугадайку числа в диапазоны [1, 100] и [1, 10].
Если не входят, вызывать функцию со случайными числами
из диапазонов.
"""
from functools import wraps

from tsk1 import get_num
from random import randint


def check_values(func):
    @wraps(func)
    def wrapper(quest, attempts):
        if quest < 1 or quest > 100:
            quest = randint(1, 100)
        if attempts < 1 or attempts > 10:
            attempts = randint(1, 10)
        res = func(quest, attempts)
        return res

    return wrapper


@check_values
def quiz(quest, attempts):
    while attempts != 0:
        print('Отгадайте число: ')
        ans = get_num(max_value=100)
        if ans == quest:
            return 'Вы угадали'
        if ans > quest:
            print('Не верно, загаданное число меньше')
        else:
            print('Не верно, загаданное число больше')
        attempts -= 1
    return f'Вы проиграли, верный ответ {quest}'


if __name__ == '__main__':
    print(quiz(10, 5))
