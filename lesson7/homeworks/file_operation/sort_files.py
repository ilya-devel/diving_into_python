"""
✔ Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
✔ Каждая группа включает файлы с несколькими расширениями.
✔ В исходной папке должны остаться только те файлы, которые не подошли для сортировки.
"""
from os import listdir, sep, walk
import shutil
from pathlib import Path

EXTENSIONS = {
    'video': ['.mp4', '.mov', '.mkv'],
    'document': ['.doc', '.txt', '.opt'],
    'music': ['.mp3', 'wav', '.flac']
}


def some_sort_files(path_sort='some_data/tsk6'):
    some_path = Path().cwd() / 'some_data' / 'tsk7'
    for file in listdir(path_sort):
        for type_format, extensions in EXTENSIONS.items():
            if "." + file.split('.')[-1] in extensions:
                Path(f"{some_path}{sep}{type_format}").mkdir(parents=True, exist_ok=True)
                shutil.move(f"{path_sort}{sep}{file}", Path(some_path / type_format))


def some_sort_files_with_walk(path_sort='some_data/tsk6'):
    some_path = Path().cwd() / 'some_data' / 'tsk7'
    for root, dirs, files in walk(path_sort):
        for file in files:
            for type_format, extensions in EXTENSIONS.items():
                if "." + file.split('.')[-1] in extensions:
                    Path(some_path / type_format).mkdir(parents=True, exist_ok=True)
                    shutil.move(f"{root}{sep}{file}", Path(some_path / type_format))


if __name__ == '__main__':
    some_sort_files_with_walk()
