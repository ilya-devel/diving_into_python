"""
Доработаем задачи 3 и 4. Создайте класс проекта, который
имеет следующие методы:
загрузка данных (функция из задания 4)
вход в систему - требует указать имя и id пользователя. Для
проверки наличия пользователя в множестве используйте
магический метод проверки на равенство пользователей.
Если такого пользователя нет, вызывайте исключение
доступа. А если пользователь есть, получите его уровень из
множества пользователей.
добавление пользователя. Если уровень пользователя
меньше, чем ваш уровень, вызывайте исключение уровня
доступа.
"""

from tsk4 import load_json, Employee
from tsk3 import MyException
from pathlib import Path

PATH = Path.cwd() / 'employee.json'

__lst_employee = []
load_json(PATH, __lst_employee)


class NoFoundEmployeeError(MyException):
    def __init__(self, name, personal_id):
        self.value = name
        self.personal_id = personal_id

    def __str__(self):
        return f"Сотрудник с именем {self.value} и персональным ИД {self.personal_id} отсутствует в базе"


class AccessError(MyException):
    def __init__(self):
        pass

    def __str__(self):
        return f"Уровень доступа не достаточен"


def authorize():
    name = input("Введите имя: ")
    personal_id = input("Введите персональный id: ")
    tmp = Employee(name=name, stage=7, personal_id=personal_id)
    for emp in __lst_employee:
        if tmp == emp:
            return emp
    raise NoFoundEmployeeError(name, personal_id)


def search_emp(user):
    name = input("Введите имя: ")
    personal_id = input("Введите персональный id: ")
    tmp = Employee(name=name, stage=7, personal_id=personal_id)
    for emp in __lst_employee:
        if tmp == emp:
            if emp.stage < user.stage:
                raise AccessError()
            return emp
    raise NoFoundEmployeeError(name, personal_id)


if __name__ == '__main__':
    try:
        admin = authorize()
        try:
            print(search_emp(admin))
        except AccessError as err:
            print(err)
    except NoFoundEmployeeError as err:
        print(err)
