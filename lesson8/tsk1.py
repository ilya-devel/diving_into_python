"""
Вспоминаем задачу 3 из прошлого семинара. Мы сформировали
текстовый файл с псевдо именами и произведением чисел.
Напишите функцию, которая создаёт из созданного ранее
файла новый с данными в формате JSON.
Имена пишите с большой буквы.
Каждую пару сохраняйте с новой строки.
"""
import json
from pathlib import Path

some_file = Path.cwd() / '..' / 'lesson7' / 'some_data' / 'tsk3_data.txt'
path_to_file = Path.cwd() / 'some_data'
some_json = path_to_file / 'tsk1.json'


def some_function(file_from, file_to):
    if not file_from.is_file():
        raise Exception("Отсутствует файл источник")
    some_json.touch(exist_ok=True)
    with (open(file_from, 'r', encoding='UTF-8') as from_file,
          open(file_to, 'w', encoding='UTF-8') as to_file):
        tmp_dict = dict()
        for row in from_file.readlines():
            key, value = row.strip().split()
            tmp_dict[key.capitalize()] = value
        json.dump(tmp_dict, to_file, indent=2)


if __name__ == '__main__':
    Path(path_to_file).mkdir(parents=True, exist_ok=True)
    try:
        some_function(some_file, some_json)
    except Exception as err:
        print(err)
