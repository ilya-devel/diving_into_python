"""
✔ Доработаем предыдущую задачу.
✔ Создайте новую функцию которая генерирует файлы с разными расширениями.
✔ Расширения и количество файлов функция принимает в качестве параметров.
✔ Количество переданных расширений может быть любым.
✔ Количество файлов для каждого расширения различно.
✔ Внутри используйте вызов функции из прошлой задачи.
"""

from tsk4 import some_func


def some_func_ver2(extensions_count: dict, path='tsk5'):
    for ext, amount in extensions_count.items():
        some_func(extension=ext, amount=amount, path=path)


if __name__ == '__main__':
    some_dict = {
        'txt': 5,
        'doc': 3
    }
    some_func_ver2(some_dict)
