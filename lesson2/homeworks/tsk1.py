"""
Напишите программу, которая получает целое
число и возвращает его шестнадцатеричное
строковое представление. Функцию hex
используйте для проверки своего результата.
"""

HEX = 16
SIMBOLS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E', 'F']


def get_hex_value(value: int):
    result = ""
    while value > 0:
        result = str(SIMBOLS[value % HEX]) + result
        value //= HEX
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
print(f"{hex(num)} == 0x{get_hex_value(num)}")
