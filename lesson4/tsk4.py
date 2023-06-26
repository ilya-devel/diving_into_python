"""
Функция получает на вход список чисел.
Отсортируйте его элементы in place без использования встроенных в язык сортировок.
Как вариант напишите сортировку пузырьком.
Её описание есть в википедии.
"""
from random import randint


def bubble_sort(raw_lst: list):
    check = True
    while check:
        check = False
        for i in range(len(raw_lst) - 1):
            if raw_lst[i] > raw_lst[i + 1]:
                tmp = raw_lst[i]
                raw_lst[i] = raw_lst[i + 1]
                raw_lst[i + 1] = tmp
                check = True
    return raw_lst


def fast_sort(raw_lst: list):
    if len(raw_lst) == 1 or len(raw_lst) == 0:
        return raw_lst
    else:
        return fast_sort([i for i in raw_lst[1:] if i <= raw_lst[0]]) + [raw_lst[0]] + fast_sort(
            [i for i in raw_lst[1:] if i > raw_lst[0]])


quick = lambda l: quick([x for x in l[1:] if x <= l[0]]) + [l[0]] + quick([x for x in l[1:] if x > l[0]]) if l else []

lst = [randint(1, 10) for _ in range(10)]
print(f"{lst = }")
print(f"{bubble_sort(lst.copy()) = }")
print(f"{fast_sort(lst.copy()) = }")
print(f"{quick(lst.copy()) = }")
