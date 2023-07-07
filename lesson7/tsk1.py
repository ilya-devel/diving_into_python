"""
✔ Напишите функцию, которая заполняет файл
(добавляет в конец) случайными парами чисел.
✔ Первое число int, второе - float разделены вертикальной чертой.
✔ Минимальное число - -1000, максимальное - +1000.
✔ Количество строк и имя файла передаются как аргументы функции.
"""
from os import sep
from pathlib import Path
from random import randint, random


def put_numbers_in_file(count_rows: int, file_name: str):
    some_path = Path.cwd() / 'some_data'
    Path(some_path).mkdir(parents=True, exist_ok=True)
    with open(f'{some_path}{sep}{file_name}', 'w', encoding='UTF-8') as f:
        for _ in range(count_rows):
            print(f'{randint(-1000, 1000)} / {random():0.2f}', file=f)


if __name__ == '__main__':
    put_numbers_in_file(3, 'tsk1_data.txt')
