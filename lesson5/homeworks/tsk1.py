"""
 Напишите функцию, которая принимает на вход строку —
абсолютный путь до файла. Функция возвращает кортеж из трёх
элементов: путь, имя файла, расширение файла.
"""

from os import sep as s


def get_data_from_path(path: str):
    path, file_ = path.rsplit(s, maxsplit=1)
    name, extension = file_.split(".")
    return path, name, extension


some_path = input("Введите путь к файлу: ")
p, n, e = get_data_from_path(some_path)
print(f"Файл с именем {n} и расширением {e}, находится в папке: {p}")
