"""
Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY
Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
Для простоты договоримся, что год может быть в диапазоне [1, 9999].
Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь.
Проверку года на високосность вынести в отдельную защищённую функцию
"""

from datetime import datetime as dt


def date_is_valid(date: str):
    try:
        dt.strptime(date, "%d.%m.%Y")
        return True
    except ValueError:
        return False


if __name__ == '__main__':
    print(date_is_valid("29.02.2019"))
    print(date_is_valid("29.02.2018"))
    print(date_is_valid("29.02.2017"))
    print(date_is_valid("29.02.2016"))
    print(date_is_valid("1998.12.01"))
