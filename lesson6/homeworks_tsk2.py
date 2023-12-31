"""
Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него напишите код, решающий задачу о 8 ферзях.
Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга.
Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
Если ферзи не бьют друг друга верните истину, а если бьют - ложь.

!!! Для корректной работы необходимо вместе с задачей скачать пакет "tsk8package"
"""

from tsk8package.chess import ChessDesk

if __name__ == '__main__':
    desk1 = ChessDesk()
    desk1.show_desk()
    print(f"Результат проверки на пересечение движения ферзей: {desk1.check_shah()}")
    print()
    desk2 = ChessDesk([(i, i) for i in range(8)])
    desk2.show_desk()
    print(f"Результат проверки на пересечение движения ферзей: {desk2.check_shah()}")
