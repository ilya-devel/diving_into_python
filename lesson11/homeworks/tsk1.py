"""
Создайте класс Матрица. Добавьте методы для:
○ вывода на печать,
○ сравнения,
○ сложения,
○ умножения матриц
"""


class MatrixArray:
    """
    Данный класс создаёт экземпляр двумерной матрицы по полученному массиву, если переданный массив верен
    """

    def __init__(self, matrix):
        if len(set(map(len, matrix))) != 1:
            raise "Данная матрица не возможна"
        self.count_row = len(matrix)
        self.count_col = len(matrix[0])
        self.matrix = matrix

    def __add__(self, other):
        """
        Выполняет сложение двух экземпляров класса, если это возможно
        :param other:
        :return:
        """
        if self.count_row != other.count_row or self.count_col != other.count_col:
            raise "Сложение матриц возможно только в случае одинаковых по количеству строк и столбцов"
        new_matrix = []
        for x in range(self.count_row):
            row = []
            for y in range(self.count_col):
                row.append(self.matrix[x][y] + other.matrix[x][y])
            new_matrix.append(row)
        return MatrixArray(new_matrix)

    def __mul__(self, other):
        """
        Выполняет умножение двух экземпляров класса, если это возможно
        :param other:
        :return:
        """
        if self.count_col != other.count_row:
            raise "Операция умножения двух матриц выполнима только в том случае, " \
                  "если число столбцов в первом сомножителе равно числу строк во втором"
        new_matrix = []
        for x in range(self.count_row):
            row = []
            for y in range(other.count_col):
                res = 0
                for z in range(self.count_col):
                    res += self.matrix[x][z] * other.matrix[z][y]
                row.append(res)
            new_matrix.append(row)

        return MatrixArray(new_matrix)

    def __str__(self):
        m_ = max([len(str(num)) for el in self.matrix for num in el])
        msg = '\n'.join([' '.join([f"{num:>{m_}}" for num in el]) for el in self.matrix])
        return msg

    def __eq__(self, other):
        return self.matrix == other.matrix


if __name__ == '__main__':
    matrix1 = MatrixArray([
        [1, 1, 2, 3, 4],
        [1213, 23, 123, 12, 12]
    ])
    matrix2 = MatrixArray([
        [5, 4, 3, 2, 1],
        [1, 2, 3, 4, 5],
    ])
    matrix3 = MatrixArray([
        [5, 4, 3, 2, 1],
        [1, 2, 3, 4, 5],
        [3, 3, 3, 3, 3],
    ])
    matrix4 = MatrixArray([
        [1, 2, 5],
        [1, 2, 3],
        [1, 2, 2],
        [1, 2, 4],
        [1, 2, 1]
    ])
    matrix5 = MatrixArray([
        [5, 4, 3, 2, 1],
        [1, 2, 3, 4, 5],
    ])
    print(matrix1 + matrix2)
    print()
    print(matrix3 * matrix4)
    print(matrix3 == matrix4)
    print(matrix2 == matrix5)
