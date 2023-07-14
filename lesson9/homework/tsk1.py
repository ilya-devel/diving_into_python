"""
Напишите следующие функции:
○ Нахождение корней квадратного уравнения
○ Генерация csv файла с тремя случайными числами в каждой строке.
100-1000 строк.
○ Декоратор, запускающий функцию нахождения корней квадратного
уравнения с каждой тройкой чисел из csv файла.
○ Декоратор, сохраняющий переданные параметры и результаты работы
функции в json файл.
Соберите пакет с играми из тех файлов, что уже были созданы в рамках курса
"""
import csv
import json
import os
from random import randint
from functools import wraps
from pathlib import Path

HEADERS = ['A', 'B', 'C']
FILE = Path().cwd() / 'data.csv'
FJSON = Path().cwd() / 'result.json'


def send_three_values_from_file(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        with open(FILE, 'r', encoding='UTF-8') as f:
            reader = csv.DictReader(f, fieldnames=HEADERS, dialect='excel-tab', quoting=csv.QUOTE_NONNUMERIC)
            for row in reader:
                func(**row)

    return wrapper


def write_info_about_work_to_json(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        with open(FJSON, 'r', encoding='UTF-8') as f:
            try:
                tmp_lst = json.load(f)
            except Exception as err:
                print(err)
                tmp_lst = []
        with open(FJSON, 'w', encoding='UTF-8') as f:
            res = func(*args, **kwargs)
            kwargs['result'] = str(res)
            tmp_lst.append(kwargs)
            json.dump(tmp_lst, f, indent=2)

    return wrapper


def create_csv_with_data():
    with open(FILE, 'w', encoding='UTF-8') as f:
        writer = csv.DictWriter(f, fieldnames=HEADERS, dialect='excel-tab')
        for _ in range(randint(100, 1000)):
            writer.writerow({key: randint(1, 100) for key in HEADERS})


@send_three_values_from_file
@write_info_about_work_to_json
def find_roots_quadratic_equation(A=1, B=1, C=1):
    d = (B ** 2) - (4 * A * C)
    if d < 0:
        d = complex((B ** 2) - (4 * A * C))
        return ((-B + d ** 0.5) / 2 * A), ((-B - d ** 0.5) / 2 * A)
    elif d == 0:
        return -B / 2 * A
    else:
        return ((-B + d ** 0.5) / 2 * A), ((-B - d ** 0.5) / 2 * A)


if __name__ == '__main__':
    if FILE.is_file():
        os.remove(FILE)
    create_csv_with_data()
    find_roots_quadratic_equation()
