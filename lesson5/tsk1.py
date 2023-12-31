"""
✔ Пользователь вводит строку из четырёх
или более целых чисел, разделённых символом “/”.
Сформируйте словарь, где:
✔второе и третье число являются ключами.
✔первое число является значением для первого ключа.
✔четвертое и все возможные последующие числа
 хранятся в кортеже как значения второго ключа.
"""


def get_some_dict(row: str):
    a, b, c, *d = row.split("/")
    return {b: a, c: tuple(d)}


some_row = "123/4141/1414/141/12937/1238"

print(get_some_dict(some_row))
