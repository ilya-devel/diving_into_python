"""
Дан список повторяющихся элементов.
Вернуть список с дублирующимися элементами.
В результирующем списке не должно быть дубликатов.
"""

from random import randint

lst = [randint(0, 10) for _ in range(20)]

print(f"Дан список: {', '.join(map(str, lst))}")

dub_lst = []

for i in range(len(lst), 0, -1):
    if lst.count(lst[i-1]) > 1:
        dub_lst.append(lst.pop(i-1))

print(f"Основной список после очистки от дубликатов: {', '.join(map(str, lst))}")
print(f"Список с дубликатами: {', '.join(map(str, dub_lst))}")
