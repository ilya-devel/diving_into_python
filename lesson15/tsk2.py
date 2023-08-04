"""
📌На семинаре про декораторы был создан логирующий
декоратор. Он сохранял аргументы функции и результат её
работы в файл.
📌Напишите аналогичный декоратор, но внутри используйте
модуль logging.
"""

import logging
from pathlib import Path
from functools import wraps

DIR_LOGS = Path.cwd() / 'logs'
FORMAT_MSG = "{asctime} {levelname}: {msg}\n"


def get_logger():
    if not DIR_LOGS.is_dir():
        DIR_LOGS.mkdir()
    logging.basicConfig(filename='logs/tsk2.log', filemode='a', encoding='utf-8', level=logging.DEBUG, style='{',
                        format=FORMAT_MSG)
    return logging.getLogger()


logger = get_logger()


def logging_function(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logger.info(
            f"{func.__name__}: args = {args}\nkwargs = {kwargs}")
        result = func(*args, **kwargs)
        return result

    return wrapper


@logging_function
def some_func(*args, **kwargs):
    msg = f"args = {args}\nkwargs = {kwargs}"
    return msg


if __name__ == '__main__':
    print(some_func(1, 5, 's', 123, key=123, som="less"))
