"""
Напишите класс для хранения информации о человеке:
ФИО, возраст и т.п. на ваш выбор.
У класса должны быть методы birthday для увеличения
возраста на год, full_name для вывода полного ФИО и т.п. на
ваш выбор.
Убедитесь, что свойство возраст недоступно для прямого
изменения, но есть возможность получить текущий возраст.
"""
from datetime import datetime as dt


class Person:
    def __init__(self, surname="Anonim", name="Anonim", patronymic="Anonim", age=1,
                 birthday=dt.now().strftime("%d.%m.%Y")):
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.__age = age
        self.birthdays = self.format_birthday(birthday)

    @staticmethod
    def format_birthday(date):
        try:
            return dt.strptime(date, "%d.%m.%Y").strftime("%d.%m.%Y")
        except Exception as err:
            print("Формат даты указан не верно, принята текущая дата")
            return dt.now().strftime("%d.%m.%Y")

    def get_age(self):
        return self.__age

    def get_fullname(self):
        return f"{self.surname} {self.name} {self.patronymic}"

    def birthday(self):
        self.__age += 1

    def __str__(self):
        return f"{self.get_fullname()}, {self.get_age()} год(а) и день рождения {self.birthdays}"


if __name__ == '__main__':
    print(Person())
    person = Person("Пушкин", "Александр", "Сергеевич", 31, "30.02.1988")
    print(person)
    person.birthday()
    print(person)
