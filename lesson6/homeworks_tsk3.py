"""
Напишите функцию в шахматный модуль.
Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше.
Проверяйте различный случайные варианты и выведите 4 успешных расстановки.

!!! Для корректной работы необходимо вместе с задачей скачать пакет "tsk8package"
"""

from tsk8package.chess import ChessDesk, generate_position


def get_true_result():
    lst_true_result = []
    while len(lst_true_result) < 4:
        queens = generate_position()
        if ChessDesk(queens).check_shah():
            lst_true_result.append(queens)
    return lst_true_result


if __name__ == '__main__':
    print(*get_true_result(), sep="\n")