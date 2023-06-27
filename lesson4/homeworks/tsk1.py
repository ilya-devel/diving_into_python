"""
Напишите функцию для транспонирования матрицы
"""
from random import randint


def trans_matrix(matrix2d: list[list]):
    return [[row[ind] for row in matrix2d] for ind in range(len(matrix2d[0]))]


if __name__ == '__main__':
    matrix = [[randint(1, 10) for _ in range(3)] for _ in range(2)]
    print('Main matrix:')
    for i in matrix:
        print('\t'.join(map(str, i)))
    print('\nTransformed matrix:')
    for i in trans_matrix(matrix):
        print('\t'.join(map(str, i)))
