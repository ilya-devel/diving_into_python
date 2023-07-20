"""
Доработаем класс Архив из задачи 2.
Добавьте методы представления экземпляра для программиста
и для пользователя.
"""

from tsk2 import Archive


class ArchiveSecond(Archive):
    def __str__(self):
        return f"Строка: {self.row}\nЧисло: {self.num}"

    def __repr__(self):
        return f"Archive(row={self.row},num={self.num})"


if __name__ == '__main__':
    ArchiveSecond()
    for obj in ArchiveSecond.get_lst_archives():
        print(obj)
        print()
        print(repr(obj))
