import sys

lst = [1, 2.3, "string", [1, 2], True, {'one': 1, 'two': 2}, (1, 2, 3), {1, 2, 3}, frozenset([1, 2, 3])]

for num, data in enumerate(lst):
    print(f"{num + 1}. Рассматриваем данные: {data}")
    print(f"\tАдрес в памяти: {id(data)}")
    print(f"\tРазмер в памяти: {sys.getsizeof(data)}")
    print(f"\tХэш объекта: {hash(data) if type(data) not in [list, dict, set] else 'Объект не хэшируемый'}")
    print(f"\t{'Это число' if isinstance(data, int) else 'Это не число'}")
    print(f"\t{'Это строка' if isinstance(data, str) else 'Это не строка'}")
    print()
