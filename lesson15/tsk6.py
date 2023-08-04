"""
📌Напишите код, который запускается из командной строки и получает на вход
путь до директории на ПК.
📌Соберите информацию о содержимом в виде объектов namedtuple.
📌Каждый объект хранит:
○ имя файла без расширения или название каталога,
○ расширение, если это файл,
○ флаг каталога,
○ название родительского каталога.
📌В процессе сбора сохраните данные в текстовый файл используя
логирование.
"""

import argparse
import os
from collections import namedtuple
from pathlib import Path
import logging

DIR_LOGS = Path.cwd() / 'logs'
FORMAT_MSG = "{asctime} {levelname} {funcName}: {msg}"

DirFileObject = namedtuple('DirFileObject', ['name_obj', 'extension', 'is_directory', 'parent_dir'])

lst_obj = []


def get_logger(filename='logs/tsk6.log'):
    if not DIR_LOGS.is_dir():
        DIR_LOGS.mkdir()
    logging.basicConfig(filename=filename, filemode='w', encoding='utf-8', level=logging.DEBUG, style='{',
                        format=FORMAT_MSG)
    return logging.getLogger()


logger = get_logger()


def parse_directory(path: Path):
    if not path.is_dir():
        logger.warning(f"Папка {path} не существует или к ней нет доступа\n")
        return None
    logger.info(f"Начинаем парсинг директории {path}")
    paths = [path]
    while paths:
        tmp_path = paths.pop()
        for elem in os.listdir(tmp_path):
            if Path(Path(tmp_path) / elem).is_dir():
                paths.append(Path(tmp_path)/elem)
            obj = get_object(tmp_path, elem)
            lst_obj.append(obj)
            logger.info(f"Объект {obj} добавлен в лог")
    logger.info(f"Работа завершена\n{'==' * 30}")
    pass


def get_object(root: Path, obj: str):
    name_obj, extension = obj.rsplit('.', maxsplit=1) if '.' in obj and Path(root / obj).is_file() else (obj, '')
    is_directory = Path(Path(root) / obj).is_dir()
    parent_dir = str(root).rsplit(os.sep)[-1]
    return DirFileObject(name_obj, extension, is_directory, parent_dir)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Парсер папки")
    parser.add_argument('path', metavar='PATH', type=str, nargs='?', default=Path.cwd())
    args = parser.parse_args()
    parse_directory(Path(args.path))
