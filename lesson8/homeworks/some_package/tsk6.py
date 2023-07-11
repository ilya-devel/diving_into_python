"""
Напишите функцию, которая преобразует pickle файл
хранящий список словарей в табличный csv файл.
Для тестированию возьмите pickle версию файла из задачи
4 этого семинара.
Функция должна извлекать ключи словаря для заголовков
столбца из переданного файла.
"""
import csv
import json
from pathlib import Path
import pickle

PATH = Path.cwd() / 'some_data'
SOME_JSON = PATH / 'tsk4.json'
SOME_CSV = PATH / 'tsk6.csv'
SOME_PICKLE = PATH / 'tsk6.bin'


def get_pickle_file():
    if not SOME_JSON.is_file():
        raise Exception("Отсутствует файл источник json")
    with open(SOME_JSON, 'r', encoding='UTF-8') as file_json:
        tmp_dir = json.load(file_json)
    with open(SOME_PICKLE, 'wb') as file_pickle:
        pickle.dump(tmp_dir, file_pickle, protocol=pickle.DEFAULT_PROTOCOL)


def some_function(some_pickle, some_csv):
    if not some_pickle.is_file():
        raise Exception("Отсутствует файл источник")
    with open(some_pickle, 'rb') as file:
        tmp_dict = pickle.load(file)
    headers = ['hash_id']
    for key in tmp_dict.keys():
        for k in tmp_dict[key].keys():
            headers.append(k)
    with open(some_csv, 'w', encoding='UTF-8') as file_csv:
        writer = csv.DictWriter(file_csv, fieldnames=sorted(set(headers)), dialect='excel-tab')
        writer.writeheader()
        lst = []
        for key in tmp_dict.keys():
            t_dict = {'hash_id': key}
            for k in tmp_dict[key].keys():
                t_dict[k] = tmp_dict[key][k].strip() if isinstance(tmp_dict[key][k].strip(), str) else tmp_dict[key][k].strip()
            lst.append(t_dict)
        writer.writerows(lst)


if __name__ == '__main__':
    Path(PATH).mkdir(parents=True, exist_ok=True)
    try:
        get_pickle_file()
        some_function(SOME_PICKLE, SOME_CSV)
    except Exception as err:
        print(err)
