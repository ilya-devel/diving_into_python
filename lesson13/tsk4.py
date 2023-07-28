"""
Вспоминаем задачу из семинара 8 про сериализацию данных,
где в бесконечном цикле запрашивали имя, личный
идентификатор и уровень доступа (от 1 до 7) сохраняя
информацию в JSON файл.
Напишите класс пользователя, который хранит эти данные в
свойствах экземпляра.
Отдельно напишите функцию, которая считывает информацию
из JSON файла и формирует множество пользователей.
"""
import json
from pathlib import Path

from lesson12.homeworks.descriptors import Range

LST_EMPLOYEE = []
PATH = Path.cwd() / 'employee.json'


class Employee:
    stage = Range(1, 7)

    def __init__(self, name, stage, personal_id):
        self.name = name
        self.stage = stage
        self.personal_id = personal_id

    def __str__(self):
        return f"Name = {self.name}, stage = {self.stage}, personal_id = {self.personal_id}"

    def __repr__(self):
        return f"Employee(\"{self.name}\", {self.stage}, \"{self.personal_id}\")"

    def get_dict_about(self):
        return {'name': self.name, 'stage': self.stage, 'personal_id': self.personal_id}

    def __eq__(self, other):
        return self.name == other.name and self.personal_id == other.personal_id


def get_employee():
    name = input("Введите имя: ")
    stage = int(input("Введите уровень доступа: "))
    personal_id = input("Введите персональный id: ")
    return Employee(name=name, stage=stage, personal_id=personal_id)


def save_json(path=PATH):
    with open(path, 'w', encoding='UTF-8') as f:
        json.dump([emp.get_dict_about() for emp in LST_EMPLOYEE if type(emp) is Employee], f)


def load_json(path=PATH, lst=None):
    if lst is None:
        lst = LST_EMPLOYEE
    if not path.is_file():
        return
    with open(path, 'r', encoding='UTF-8') as f:
        tmp = json.load(f)
    for emp in tmp:
        lst.append(Employee(**emp))


if __name__ == '__main__':
    load_json()
    print(f"{LST_EMPLOYEE = }")
    for _ in range(2):
        LST_EMPLOYEE.append(get_employee())
    save_json()
    LST_EMPLOYEE = []
