"""
Создайте класс Сотрудник.
Воспользуйтесь классом человека из прошлого задания.
У сотрудника должен быть:
○ шестизначный идентификационный номер
○ уровень доступа вычисляемый как остаток от деления
суммы цифр id на семь
"""
from tsk3 import Person


class Employee(Person):
    def __init__(self, id_="000016", *args, **kwargs):
        self.id = id_
        self.access_level = self.set_access_level()
        super().__init__(*args, **kwargs)

    def set_access_level(self):
        return sum(map(int, self.id)) % 7

    def get_id(self):
        return self.id

    def get_access_level(self):
        return self.access_level

    def __str__(self):
        return super(Employee, self).__str__() + f"id = {self.id}, access_level = {self.access_level}"


if __name__ == '__main__':
    person = Employee()
    print(person)
