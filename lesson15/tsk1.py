"""
📌Напишите программу, которая использует модуль logging для
вывода сообщения об ошибке в файл.
📌Например отлавливаем ошибку деления на ноль.
"""

import logging
from pathlib import Path

DIR_LOGS = Path.cwd() / 'logs'

if not DIR_LOGS.is_dir():
    DIR_LOGS.mkdir()

FORMAT_MSG = "{asctime} {levelname} {funcName}: {msg}"
logging.basicConfig(filename='logs/tsk1.log', filemode='a', encoding='utf-8', level=logging.DEBUG, style='{',
                    format=FORMAT_MSG)
logger = logging.getLogger()


def some_func(a: int | float, b: int | float):
    if b == 0:
        logger.warning(f"На ноль делить нельзя: {float('inf')}")
        return float('inf')
    logger.info(f"Результат {a}/{b} равен: {a / b}")
    return a / b


if __name__ == '__main__':
    some_func(3, 5)
    some_func(3.1, 1.3)
    some_func(3, 0)
