"""
Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
Достаточно вернуть один допустимый вариант.

*Верните все возможные варианты комплектации рюкзака.
"""

import itertools

BAG_SIZE = 60

items = {
    "axe": 30,
    "knife": 10,
    "club": 25,
    "sword": 15,
    "iron_ball": 60
}


def get_all_size(keys: list[str], d: dict):
    return sum([d[key] for key in keys])


all_variables = []
for i in itertools.product(items.keys(), repeat=len(items.keys())):
    if set(sorted(i)) not in all_variables and get_all_size(list(set(i)), items) <= BAG_SIZE:
        all_variables.append(set(sorted(i)))

print("Возможные вариации комплектации рюкзака: ")
for v in all_variables:
    print(f"\t{', '.join(v)}")
