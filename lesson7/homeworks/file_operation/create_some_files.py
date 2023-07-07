"""
✔ Дорабатываем функции из предыдущих задач.
✔ Генерируйте файлы в указанную директорию — отдельный параметр функции.
✔ Отсутствие/наличие директории не должно вызывать ошибок в работе функции
(добавьте проверки).
✔ Существующие файлы не должны удаляться/изменяться в случае совпадения имён
"""

from pathlib import Path
from random import randint, choices
from os import getrandom, sep, listdir


def some_func(extension='txt', min_length=6, max_length=30, min_bytes=256, max_bytes=4096, amount=42, path='tsk4'):
    characters = 'abcdefghijklmnopqrstuvwxyz0123456789'
    some_path = Path().cwd() / path
    Path(some_path).mkdir(parents=True, exist_ok=True)
    for _ in range(amount):
        name = ''.join(choices(characters, k=randint(min_length, max_length)))
        count = 1
        if f"{name}.{extension}" in listdir(some_path):
            while f"{name}_{count}.{extension}" in listdir(some_path):
                count += 1
            name = f"{name}_{count}"
        file_name = f"{name}.{extension}"
        with open(f"{some_path}{sep}{file_name}", 'wb') as f:
            f.write(getrandom(randint(min_bytes, max_bytes)))


def some_func_ver2(extensions_count: dict, path='tsk5'):
    for ext, amount in extensions_count.items():
        some_func(extension=ext, amount=amount, path=path)


if __name__ == '__main__':
    some_dict = {
        'txt': 5,
        'doc': 3,
        'mkv': 3,
        'mp3': 2,
        'flac': 5,
        'ini': 2,
    }
    some_func_ver2(some_dict, path='tsk6')
