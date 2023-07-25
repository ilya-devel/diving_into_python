import csv
import re
from pathlib import Path


class CheckName:
    def __init__(self, name: str = None):
        self.name = name

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)

    def __delete__(self, instance):
        raise AttributeError(f"Свойство {self.param_name} нельзя удалять")

    @staticmethod
    def validate(value):
        if not isinstance(value, str) or not value:
            raise TypeError(f"Значение {value} должно быть не пустой строкой")
        if value != value.capitalize():
            raise ValueError(f"Значение {value} должно начинаться с заглавной буквы")
        if re.search(r"\d", value):
            raise ValueError(f"Значение {value} должно не должно содержать чисел")


class GetListSubjects:
    def __init__(self, value: str = None):
        self.subjects = value

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        try:
            if getattr(instance, self.param_name):
                raise AttributeError(f"Свойство {self.param_name} нельзя изменять")
        except AttributeError as err:
            setattr(instance, self.param_name, self.get_subjects(value))
        except Exception as err:
            raise Exception(f"Возникла ошибка: {err}")

    def __delete__(self, instance):
        raise AttributeError(f"Свойство {self.param_name} нельзя удалять")

    @staticmethod
    def validate(value):
        if not Path(value).is_file():
            raise FileNotFoundError(f"Файл {value} не доступен или отсутствует")
        if not str(value).endswith('.csv'):
            raise ValueError(f"Списком предметов должен быть в файле csv")
        if value is None:
            raise ValueError(f"Не указан путь к файлу со списком предметов")

    @staticmethod
    def get_subjects(path_to_file) -> dict:
        with open(path_to_file, 'r', encoding='UTF-8') as f:
            subjects = dict()
            try:
                for row in csv.DictReader(f):
                    subjects[row['subjects']] = {
                        'test_values': [],
                        'subject_value': 0
                    }
            except Exception as err:
                raise Exception(f"Нет столбца subjects в файле: {err}")
            return subjects


class Range:
    def __init__(self, min_value: int = None, max_value: int = None):
        self.min_value = min_value
        self.max_value = max_value

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)

    def __delete__(self, instance):
        raise AttributeError(f"Свойство {self.param_name} нельзя удалять")

    def validate(self, value):
        if not isinstance(value, int):
            raise TypeError(f"Значение {value} должно быть целым числом")
        if self.min_value is not None and value < self.min_value:
            raise ValueError(f"Значение {value} должно быть больше или равно {self.min_value}")
        if self.max_value is not None and value > self.max_value:
            raise ValueError(f"Значение {value} должно быть меньше или равно {self.min_value}")


if __name__ == '__main__':
    pass
