"""
📌На семинаре 13 был создан проект по работе с
пользователями (имя, id, уровень).
📌Напишите 3-7 тестов pytest для данного проекта.
📌Используйте фикстуры.
"""

from lesson13.tsk4 import Employee
import pytest


@pytest.fixture
def new_data():
    data = [
        Employee(name='Mike', stage=1, personal_id='ladfj'),
        Employee(name='Mary', stage=3, personal_id='alkjf'),
        Employee(name='Mara', stage=5, personal_id='aj;df'),
    ]
    return data


def test_stage(new_data):
    for emp in new_data:
        assert emp.__str__() == f"Name = {emp.name}, stage = {emp.stage}, personal_id = {emp.personal_id}"


def test_invalid_employee_stage():
    with pytest.raises(TypeError):
        Employee(name='Test', stage='s', personal_id='aljkf')


def test_invalid_employee_stage_diapason_max():
    with pytest.raises(ValueError):
        Employee(name='Test', stage=10, personal_id='aljkf')


def test_invalid_employee_stage_diapason_min():
    with pytest.raises(ValueError):
        Employee(name='Test', stage=0, personal_id='aljkf')


if __name__ == '__main__':
    pytest.main(['-v'])
