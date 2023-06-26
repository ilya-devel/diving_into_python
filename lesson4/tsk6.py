"""
Функция получает на вход список чисел и два индекса.
Вернуть сумму чисел между между переданными индексами.
Если индекс выходит за пределы списка, сумма считается
до конца и/или начала списка.
"""
from random import randint


def get_sum_diapason(lst_num: list, start: int, fin: int):
    if start > fin:
        return get_sum_diapason(lst_num, fin, start)
    return sum(lst_num[start: fin])


lst = [randint(1, 10) for _ in range(20)]
print(f"{lst = }")
print(f"{get_sum_diapason(lst, 3, 7) = }")
print(f"{get_sum_diapason(lst, 7, 3) = }")
