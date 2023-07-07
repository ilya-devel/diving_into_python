"""
Напишите функцию группового переименования файлов. Она должна:
✔ принимать параметр желаемое конечное имя файлов.
При переименовании в конце имени добавляется порядковый номер.
✔ принимать параметр количество цифр в порядковом номере.
✔ принимать параметр расширение исходного файла.
Переименование должно работать только для этих файлов внутри каталога.
✔ принимать параметр расширение конечного файла.
✔ принимать диапазон сохраняемого оригинального имени. Например для диапазона
[3, 6] берутся буквы с 3 по 6 из исходного имени файла. К ним прибавляется
желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.
✔ Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами.
"""
from os import walk, sep
from pathlib import Path


def rename_group_files(end_name='new_name', count_name=1, length_count=3, extension=None,
                       end_extension=None, slice_orig=None, path='../some_data/tsk6'):
    """
    Функция производит групповое переименование файлов в указанной директории
    :param end_name: Указывается желаемое имя
    :param count_name: счётчик к имени
    :param length_count: длина счётчика
    :param extension: принимает расширение или список расширений для переименования, иначе переименовывает все файлы
    :param end_extension: расширение файла после переименования
    :param slice_orig: указать списком диапазон от оригинального имени для сохранения
    :param path: путь к папке с файлами
    :return:
    """
    for root, dirs, files in walk(Path(Path().cwd() / path)):
        for file in files:
            name, ext_check = file.rsplit('.', maxsplit=1)
            if isinstance(extension, str):
                extension = [extension]
            if extension is not None and ext_check not in extension:
                continue
            new_name = ''
            if slice_orig and len(slice_orig) >= 2:
                try:
                    a, b = map(int, slice_orig[:2])
                    new_name += name[a, b + 1]
                except Exception as err:
                    print(f"Не корректный диапазон для среза {slice_orig = }")
            if end_name is not None:
                new_name += end_name
            new_name += f"_{count_name:0{length_count}d}"
            count_name += 1
            if end_extension:
                new_name += f".{end_extension}"
            else:
                new_name += f".{ext_check}"
            rename_file = Path(root + sep + file)
            rename_file.replace(root + sep + new_name)


if __name__ == '__main__':
    rename_group_files(end_name="music", extension=['mp3', 'flac'])
    # print(Path().cwd() / '..' / 'some_data' / 'tsk6')
    # for root, _, files in os.walk(Path().cwd() / '../some_data/tsk6'):
    #     for file in files:
    #         print(f'{root}{sep}{file}')
