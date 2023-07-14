"""
Напишите декоратор, который сохраняет в json файл
параметры декорируемой функции и результат, который она
возвращает. При повторном вызове файл должен
расширяться, а не перезаписываться.
Каждый ключевой параметр сохраните как отдельный ключ
json словаря.
Для декорирования напишите функцию, которая может
принимать как позиционные, так и ключевые аргументы.
Имя файла должно совпадать с именем декорируемой
функции.
"""
import json
from functools import wraps
from pathlib import Path


# PATH_JSON = Path().cwd() / 'tsk3.json'


def write_json(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            with open(f'{func.__name__}.json', 'r', encoding='UTF-8') as f:
                tmp_lst = json.load(f)
        except Exception as err:
            tmp_lst = []
        res = func(*args)
        tmp_lst.append({'args': args, 'kwargs': {key: value for key, value in kwargs.items()}, 'result': res})
        with open(f'{func.__name__}.json', 'w', encoding='UTF-8') as f:
            json.dump(tmp_lst, f, indent=2, ensure_ascii=False)
        return res

    return wrapper


@write_json
def multiply(a, b, t1=1, t2=2):
    return a * b


if __name__ == '__main__':
    print(multiply(3, 6, t1=3, t2=4))
    print(multiply(1, 3))
