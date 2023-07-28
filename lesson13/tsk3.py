"""
Создайте класс с базовым исключением и дочерние классы исключения:
○ ошибка уровня,
○ ошибка доступа.
"""
STAGE_AND_LEVELS = {'a': ['a'],
                    'b': ['a', 'b'],
                    's': ['s', 'a', 'b']}


class MyException(Exception):
    pass


class StageError(MyException):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"Уровень доступа {self.value} не существует"


class DepartmentError(MyException):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"Департамент {self.value} не существует"


class AccessError(MyException):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"Доступ к {self.value} запрещён"


def testing_error():
    while True:
        stage = input("Введите уровень доступа: ")
        try:
            if stage not in STAGE_AND_LEVELS.keys():
                raise StageError(stage)
        except StageError as err:
            print(err)
            continue
        level = input("Укажите отдел в который направляетесь: ")
        try:
            if level not in set(i for lst in STAGE_AND_LEVELS.values() for i in lst):
                raise DepartmentError(level)
            if level not in STAGE_AND_LEVELS[stage]:
                raise AccessError(level)
        except DepartmentError | AccessError as err:
            print(err)
            continue
        print("Доступ разрешён")
        break


if __name__ == '__main__':
    try:
        testing_error()
    except Exception as err:
        print(err)
