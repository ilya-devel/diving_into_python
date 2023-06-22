"""
Напишите программу, которая получает целое
число и возвращает его шестнадцатеричное
строковое представление. Функцию hex
используйте для проверки своего результата.
"""

HEX = 16
OCT = 8
BIN = 2
SIMBOLS = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E', 'F'}


def get_hex_value(value: int, sys_: int):
    result = ""
    while value > 0:
        result = str(SIMBOLS[value % sys_]) + result
        value //= sys_
    return result


def get_value():
    val = None
    while True:
        try:
            val = int(input("Введите целое положительное число для конвертации: "))
            if val <= 0:
                raise Exception("Не верно указано число")
            break
        except Exception as err:
            print(err)
            print("Вы ввели не верное значение, попробуйте ещё раз\n")
    return val


num = get_value()
print(f"{hex(num)} == 0x{get_hex_value(num, HEX)}")
print(f"{oct(num)} == 0o{get_hex_value(num, OCT)}")
print(f"{bin(num)} == 0b{get_hex_value(num, BIN)}")
