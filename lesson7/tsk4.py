"""
✔ Создайте функцию, которая создаёт файлы с указанным расширением.
Функция принимает следующие параметры:
✔ расширение
✔ минимальная длина случайно сгенерированного имени, по умолчанию 6
✔ максимальная длина случайно сгенерированного имени, по умолчанию 30
✔ минимальное число случайных байт, записанных в файл, по умолчанию 256
✔ максимальное число случайных байт, записанных в файл, по умолчанию 4096
✔ количество файлов, по умолчанию 42
✔ Имя файла и его размер должны быть в рамках переданного диапазона.
"""

from pathlib import Path
from random import randint, choices
from os import getrandom, sep


def some_func(extension='txt', min_length=6, max_length=30, min_bytes=256, max_bytes=4096, amount=42, path='tsk4'):
    characters = 'abcdefghijklmnopqrstuvwxyz0123456789'
    some_path = Path().cwd() / 'some_data' / path
    Path(some_path).mkdir(parents=True, exist_ok=True)
    for _ in range(amount):
        some_name = f"{''.join(choices(characters, k=randint(min_length, max_length)))}.{extension}"
        with open(f"{some_path}{sep}{some_name}", 'wb') as f:
            f.write(getrandom(randint(min_bytes, max_bytes)))


if __name__ == '__main__':
    some_func()
