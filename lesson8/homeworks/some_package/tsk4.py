"""
Прочитайте созданный в прошлом задании csv файл без
использования csv.DictReader.
Дополните id до 10 цифр незначащими нулями.
В именах первую букву сделайте прописной.
Добавьте поле хеш на основе имени и идентификатора.
Получившиеся записи сохраните в json файл, где каждая строка
csv файла представлена как отдельный json словарь.
Имя исходного и конечного файлов передавайте как аргументы
функции.
"""

import json
from pathlib import Path

PATH_TO_FILE = Path.cwd() / 'some_data'
SOME_JSON = PATH_TO_FILE / 'tsk4.json'
SOME_CSV = PATH_TO_FILE / 'tsk3.csv'


def some_function(path_file, csv_file):
    with (open(csv_file, 'r', encoding='UTF-8') as file_csv,
          open(path_file, 'w', encoding='UTF-8') as file_json):
        dicts_res = dict()
        for row in file_csv.readlines()[1:]:
            tmp_dict = {}
            access_level, id_, name = row.split('\t')
            name = name.capitalize()
            id_ = f'{int(id_):0{10}d}'
            hash_tab = hash(name + id_)
            tmp_dict[hash_tab] = {
                'access_level': access_level,
                'id': id_,
                'name': name}
            dicts_res.update(tmp_dict)
        json.dump(dicts_res, file_json, ensure_ascii=False)
        #     print(json.dumps(tmp_dict, ensure_ascii=False), file=file_json, sep=',')


if __name__ == '__main__':
    Path(PATH_TO_FILE).mkdir(parents=True, exist_ok=True)
    try:
        some_function(SOME_JSON, SOME_CSV)
    except Exception as err:
        print(err)
