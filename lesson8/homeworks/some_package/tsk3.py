"""
Напишите функцию, которая сохраняет созданный в
прошлом задании файл в формате CSV.
"""
import csv
import json
from pathlib import Path

PATH_TO_FILE = Path.cwd() / 'some_data'
SOME_JSON = PATH_TO_FILE / 'tsk2.json'
SOME_CSV = PATH_TO_FILE / 'tsk3.csv'


def some_function(path_file, csv_file):
    if not path_file.is_file():
        raise Exception("Отсутствует файл источник")
    if not csv_file.is_file():
        csv_file.touch(exist_ok=True)
    with open(path_file, 'r', encoding='UTF-8') as file_from:
        tmp_dir = json.load(file_from)
    with open(csv_file, 'w', encoding='UTF-8') as file_to:
        writer = csv.DictWriter(file_to, fieldnames=['access_level', 'id', 'name'], dialect='excel-tab')
        writer.writeheader()
        tmp_lst = []
        for key in tmp_dir.keys():
            for id_, name in tmp_dir[key].items():
                tmp_lst.append({
                    'access_level': key,
                    'id': id_,
                    'name': name
                })
        writer.writerows(tmp_lst)


if __name__ == '__main__':
    Path(PATH_TO_FILE).mkdir(parents=True, exist_ok=True)
    try:
        some_function(SOME_JSON, SOME_CSV)
    except Exception as err:
        print(err)
