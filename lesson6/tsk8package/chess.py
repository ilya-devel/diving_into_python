"""
Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него напишите код, решающий задачу о 8 ферзях.
Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга.
Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
Если ферзи не бьют друг друга верните истину, а если бьют - ложь.
"""
import itertools
import random


class ChessDesk:
    def __init__(self, queens=None):
        if queens is None:
            queens = [(0, 3), (1, 1), (2, 7), (3, 4), (4, 6), (5, 0), (6, 2), (7, 5)]
        self.desk = [[False for _ in range(8)] for _ in range(8)]
        self.steps = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
        for x_pos, y_pos in queens:
            self.desk[x_pos][y_pos] = True

    def check_shah(self):
        for x_ind in range(len(self.desk)):
            for y_ind in range(len(self.desk[x_ind])):
                if self.desk[x_ind][y_ind]:
                    if not self.run_checking(x_ind, y_ind):
                        return False
        return True

    def run_checking(self, x_cur, y_cur):
        for x_next, y_next in self.steps:
            x, y = x_cur + x_next, y_cur + y_next
            while True:
                x, y = x + x_next, y + y_next
                result = self.get_result(x, y)
                if result is None:
                    break
                if result:
                    return False
        return True

    def get_result(self, x, y):
        if 0 <= x < 8 and 0 <= y < 8:
            return self.desk[x][y]
        else:
            return None

    def show_desk(self):
        for row in self.desk:
            print("".join(["▢" if not col else "♕" for col in row]))


def generate_position():
    lst_all_pos = list(itertools.product(range(8), range(8)))
    lst_pos = []
    while len(lst_pos) < 8:
        lst_pos.append(lst_all_pos.pop(random.randint(0, len(lst_all_pos) - 1)))
    return lst_pos


if __name__ == '__main__':
    desk = ChessDesk()
    # queens = [(i, i) for i in range(8)]
    # queens = [(0, 3), (1, 1), (2, 7), (3, 4), (4, 6), (5, 0), (6, 2), (7, 5)]
    desk.show_desk()
    print(desk.check_shah())
