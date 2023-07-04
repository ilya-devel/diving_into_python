"""
В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.

!!! Для корректной работы необходимо вместе с задачей скачать пакет "tsk8package"
"""
from sys import argv
from tsk8package.tsk7 import date_is_valid


def show_result_of_check_date(date: str):
    if date_is_valid(date):
        return "Дата корректна"
    else:
        return "Дата некорректна"


if __name__ == '__main__':
    if len(argv) > 1:
        print(show_result_of_check_date(argv[1]))
    else:
        print("Не была передана дата для проверки")
