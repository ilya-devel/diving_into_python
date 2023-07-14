"""
Создайте декоратор с параметром.
Параметр - целое число, количество запусков декорируемой
функции.
"""
from functools import wraps


def loop(num: int = 2):
    def deco(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num):
                func(*args, **kwargs)

        return wrapper

    return deco


@loop(10)
def hello_world():
    print("Hello")


if __name__ == '__main__':
    hello_world()
    pass
