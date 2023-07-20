"""
Создайте класс Архив, который хранит пару свойств.
Например, число и строку.
При нового экземпляра класса, старые данные из ранее
созданных экземпляров сохраняются в пару списковархивов
list-архивы также являются свойствами экземпляра
"""


class Archive:
    """
    Данный класс сохраняет каждый созданный экземпляр класса в свойстве класса _LST_ARCHIVES
    """
    _LST_ARCHIVES = []

    def __init__(self, row="something text", num=0):
        """
        Создаёт экземпляр класса сохраняя переданные строку и число
        :param row:
        :param num:
        """
        self.row = row
        self.num = num
        self.add_in_lst(self)

    @classmethod
    def add_in_lst(cls, new_obj):
        cls._LST_ARCHIVES.append(new_obj)

    @classmethod
    def get_lst_archives(cls):
        return cls._LST_ARCHIVES


if __name__ == '__main__':
    Archive("tmp1", 1)
    Archive("tmp2", 2)
    Archive("tmp3", 2)
    Archive()
    tmp = Archive()
    print("Обращение к списку от имени класса")
    for obj in Archive.get_lst_archives():
        print(obj)
    print()
    print("Обращение к списку от имени экземпляра класса")
    for obj in tmp.get_lst_archives():
        print(obj)
