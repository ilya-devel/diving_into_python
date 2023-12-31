"""
Возьмите 1-3 любые задачи из прошлых семинаров (например сериализация
данных), которые вы уже решали. Превратите функции в методы класса, а
параметры в свойства. Задачи должны решаться через вызов методов
экземпляра.
"""

import csv
import json
import os
import pickle
from pathlib import Path
from datetime import datetime


class GetInfoAboutDirs:
    def __init__(self, path=Path().cwd(), file_name_for_save: str = datetime.now().strftime("%Y-%m-%d_%H-%M-%s")):
        self.root = path
        self.paths = [path]
        self.file_name = file_name_for_save
        self.lst_obj = []
        self.scan_directory_and_write_info()

    def scan_directory_and_write_info(self):
        if not self.paths[0].is_dir():
            raise Exception("Указанный каталог не доступен")
        while self.paths:
            path = self.paths.pop(0)
            for obj in os.listdir(path):
                dir_obj = {'object': obj, 'parent_dir': None, 'type_obj': None, 'size': None}
                if Path(Path(path) / obj).is_dir():
                    self.paths.append(Path(Path(path) / obj))
                    dir_obj['type_obj'] = 'directory'
                if dir_obj['type_obj'] is None:
                    dir_obj['type_obj'] = 'file'
                dir_obj['size'] = self.get_size_dir(Path(Path(path) / obj))
                dir_obj['parent_dir'] = str(path).replace(str(self.root), '')
                self.lst_obj.append(dir_obj)
        self.write_to_files()

    @staticmethod
    def get_size_dir(path):
        if path.is_file():
            return os.path.getsize(path)
        size = 0
        for root, _, files in os.walk(path):
            for file in files:
                size += os.path.getsize(Path(Path(root) / file))
        return size

    def write_to_files(self):
        with (
            open(Path(Path().cwd() / f'{self.file_name}.bin'), 'wb') as file_pickle,
            open(Path(Path().cwd() / f'{self.file_name}.json'), 'w', encoding='UTF-8') as file_json,
            open(Path(Path().cwd() / f'{self.file_name}.csv'), 'w', encoding='UTF-8') as file_csv,
        ):
            json.dump(self.lst_obj, file_json, indent=2)
            pickle.dump(self.lst_obj, file_pickle)
            writer = csv.DictWriter(file_csv, fieldnames=self.lst_obj[0].keys(), dialect='excel-tab')
            writer.writeheader()
            writer.writerows(self.lst_obj)


PATH = Path(f'/home/ilya/Unity/Hub/Editor/2021.3.17f1/Editor/BugReporter/')

if __name__ == '__main__':
    try:
        GetInfoAboutDirs()
        GetInfoAboutDirs(PATH, 'BugReporter')
        print(GetInfoAboutDirs.get_size_dir(PATH))
    except Exception as err:
        print(err)
