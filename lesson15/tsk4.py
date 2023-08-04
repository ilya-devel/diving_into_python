"""
📌Функция получает на вход текст вида: “1-й четверг ноября”, “3-
я среда мая” и т.п.
📌Преобразуйте его в дату в текущем году.
📌Логируйте ошибки, если текст не соответсвует формату.
"""

import datetime
import logging
from pathlib import Path
import re

DIR_LOGS = Path.cwd() / 'logs'
FORMAT_MSG = "{asctime} {levelname} {funcName}: {msg}\n"

WEEKDAYS = ["понедельник", "вторник", "среда", "четверг", "пятница", "суббота", "воскресенье"]
MONTHS = ["", "января", "февраля", "марта", "апреля", "мая", "июня", "июля", "августа", "сентября", "октября", "ноября",
          "декабря"]


def get_logger(filename='logs/tsk4.log'):
    if not DIR_LOGS.is_dir():
        DIR_LOGS.mkdir()
    logging.basicConfig(filename=filename, filemode='a', encoding='utf-8', level=logging.DEBUG, style='{',
                        format=FORMAT_MSG)
    return logging.getLogger()


logger = get_logger()


def parse_some_data(txt: str, logger_=logger):
    pattern = r"([1-7]-.+) ([а-я]+) ([а-я]+)"
    if not re.findall(pattern, txt):
        logger_.warning("Текст не соответствует формату")
        return None
    num_month_week, weekday, month = txt.split()
    num_month_week = int(num_month_week.split('-')[0])
    weekday = WEEKDAYS.index(weekday) if weekday in WEEKDAYS else None
    month = MONTHS.index(month) if month in MONTHS else None
    return get_date(num_month_week, weekday, month)


def get_date(num_month_week, weekday, month, year=datetime.datetime.now().year):
    if num_month_week is not None and weekday is not None and month is not None:
        count = 0
        date = datetime.datetime(year=year, month=month, day=1)
        while date.month == month:
            if date.weekday() == weekday:
                count += 1
                if count == num_month_week:
                    break
            date += datetime.timedelta(days=1)
        return date
    return None


if __name__ == '__main__':
    res = parse_some_data("1-й четверг ноября")
    if res is not None:
        print(res)
    res = parse_some_data("3-я среда мая")
    if res is not None:
        print(res)
