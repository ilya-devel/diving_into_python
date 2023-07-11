"""
✔ Напишите функцию, которая открывает на чтение созданные
в прошлых задачах файлы с числами и именами.
✔ Перемножьте пары чисел. В новый файл сохраните
имя и произведение:
✔ если результат умножения отрицательный, сохраните имя
записанное строчными буквами и произведение по модулю
✔ если результат умножения положительный, сохраните имя
прописными буквами и произведение округлённое до целого.
✔ В результирующем файле должно быть столько же строк,
сколько в более длинном файле.
✔ При достижении конца более короткого файла,
возвращайтесь в его начало.
"""
import math
from os import sep
from pathlib import Path


def some_function(file_name='tsk3_data.txt'):
    some_path = Path.cwd() / 'some_data'
    Path(some_path).mkdir(parents=True, exist_ok=True)
    with (open(f'{some_path}{sep}tsk1_data.txt', 'r', encoding='UTF-8') as numbers,
          open(f'{some_path}{sep}tsk2_data.txt', 'r', encoding='UTF-8') as names,
          open(f'{some_path}{sep}{file_name}', 'w', encoding='UTF-8') as f):
        count = max(len(numbers.readlines()), len(names.readlines()))
        numbers.seek(0, 0)
        names.seek(0, 0)
        for _ in range(count):
            row1 = numbers.readline()
            if row1 == '':
                numbers.seek(0, 0)
                row1 = numbers.readline()
            row2 = names.readline()
            if row2 == '':
                names.seek(0, 0)
                row2 = names.readline()
            a, b = [float(s.strip()) for s in row1.split('/')]
            if a * b >= 0:
                print(f"{row2.upper().strip()}, {round(a * b)}", file=f)
            if a * b < 0:
                print(f"{row2.lower().strip()}, {math.fabs(a * b)}", file=f)


if __name__ == '__main__':
    some_function()
