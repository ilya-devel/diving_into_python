"""
Функция получает на вход строку из двух чисел через пробел.
Сформируйте словарь, где ключом будет
символ из Unicode, а значением —  целое число.
Диапазон пар ключ-значение от наименьшего из введённых пользователем чисел до наибольшего включительно.
"""


def get_dict_char(row: str):
    dict_char = dict()
    for num in row.split():
        if num.isdigit():
            dict_char[chr(int(num))] = int(num)
    return dict_char


raw_row = "12 213 1231 1312 13"

for key, value in sorted(get_dict_char(raw_row).items(), key=lambda x: x[1]):
    print(f"{key} => {value}")
