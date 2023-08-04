import argparse
from pathlib import Path
import logging
from rectangle_extended import Rectangle, ArgumentNotFound, NonPositiveError, NotZeroError

DIR_LOGS = Path.cwd() / 'logs'
FORMAT_MSG = "{asctime} {levelname} {funcName}: {msg}"
LOG_NAME = 'tsk1.log'


def get_logger(filename=f'logs/{LOG_NAME}'):
    if not DIR_LOGS.is_dir():
        DIR_LOGS.mkdir()
    logging.basicConfig(filename=filename, filemode='a', encoding='utf-8', level=logging.DEBUG, style='{',
                        format=FORMAT_MSG)
    return logging.getLogger()


logger = get_logger()

if __name__ == '__main__':
    parse = argparse.ArgumentParser(description="Получение площади и длины прямоугольника по указанным размерам")
    parse.add_argument('-W', type=float, metavar='width', nargs='?', default=None, help="Ширина")
    parse.add_argument('-H', type=float, metavar='height', nargs='?', default=None, help="Высота")
    args = parse.parse_args()
    try:
        rectangle = Rectangle(length=args.H, width=args.W)
        logger.info(f'Был создан {str(rectangle).lower()}')
        print(f"Площадь прямоугольника: {rectangle.get_area()}")
        print(f"Периметр прямоугольника: {rectangle.get_perimeter()}")

    except (ArgumentNotFound, NonPositiveError, NotZeroError) as err:
        print(err)
        logger.warning(err)
