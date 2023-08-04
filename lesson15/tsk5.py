"""
📌Дорабатываем задачу 4.
📌Добавьте возможность запуска из командной строки.
📌При этом значение любого параметра можно опустить. В
этом случае берётся первый в месяце день недели, текущий
день недели и/или текущий месяц.
📌*Научите функцию распознавать не только текстовое
названия дня недели и месяца, но и числовые,
т.е не мая, а 5.
"""
import datetime

from tsk4 import parse_some_data, get_logger, get_date
import argparse

logger = get_logger(filename='logs/tsk5.log')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Парсер даты")
    parser.add_argument('date', metavar='txt', type=str, default='', nargs='*')
    parser.add_argument('-c', metavar='NUM', type=int, default=1,
                        help="Порядковый номер недели в виде целого числа")
    parser.add_argument('-y', metavar='YEAR', type=int, default=datetime.datetime.now().year,
                        help="Год в виде целого числа")
    parser.add_argument('-m', metavar='MONTH', type=int, default=datetime.datetime.now().month,
                        help="Порядковый номер месяца в виде целого числа")
    parser.add_argument('-d', metavar='WEEKDAY', type=int, default=datetime.datetime.now().weekday(),
                        help="Порядковый номер дня недели в виде целого числа от 0 до 6")
    args = parser.parse_args()
    res = None
    if args.date:
        txt = args.date[0] if len(args.date) == 1 else ' '.join(args.date)
        res = parse_some_data(txt, logger_=logger)
        if res is None:
            print("Не верный тип данных в строке. Отобразим текущую дату")
            res = get_date(args.c, args.d, args.m, args.y)
    else:
        res = get_date(args.c, args.d, args.m, args.y)
    print(res)
