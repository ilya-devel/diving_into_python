"""
Напишите функцию, которая в бесконечном цикле
запрашивает имя, личный идентификатор и уровень
доступа (от 1 до 7).
После каждого ввода добавляйте новую информацию в
JSON файл.
Пользователи группируются по уровню доступа.
Идентификатор пользователя выступает ключём для имени.
Убедитесь, что все идентификаторы уникальны независимо
от уровня доступа.
При перезапуске функции уже записанные в файл данные
должны сохраняться.
"""
import json
from pathlib import Path

path_to_file = Path.cwd() / 'some_data'
some_json = path_to_file / 'tsk2.json'


def some_function(file_write):
    if not file_write.is_file():
        file_write.touch(exist_ok=True)
    ans, name, id_, access_level = None, None, None, None
    while ans != 'no':
        name = input("Введите имя > ")
        id_ = input("Введите идентификационный номер > ")
        while True:
            access_level = input("Введите код доступа от 1 до 7 > ")
            if access_level.isdigit():
                access_level = int(access_level)
                if 1 <= access_level <= 7:
                    access_level = str(access_level)
                    break
            print("Не верно указан код доступа! Попробуйте ещё раз")

        with open(file_write, 'r', encoding="UTF-8") as file_to:
            try:
                tmp_dir = json.load(file_to)
            except Exception as err:
                tmp_dir = {f"{i}": dict() for i in range(1, 8)}
        with open(file_write, 'w', encoding="UTF-8") as file_to:
            for key in tmp_dir.keys():
                if id_ in [k for k in tmp_dir[key].keys()]:
                    print("Пользователь с таким ИД уже есть в базе!")
                    continue
            tmp_dir[access_level][id_] = name
            print('create')
            json.dump(tmp_dir, file_to, ensure_ascii=False)
        print(tmp_dir)
        while True:
            ans = input("Продолжить ввод? Yes/No > ").lower()
            if ans not in ['yes', 'no']:
                print("Не верный ответ, попробуйте ещё раз")
                continue
            break


if __name__ == '__main__':
    some_function(some_json)
