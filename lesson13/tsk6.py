"""
Доработайте классы исключения так, чтобы они выдали
подробную информацию об ошибках.
Передавайте необходимые данные из основного кода
проекта.
"""


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


class NoFoundEmployeeError(MyException):
    def __init__(self, name, personal_id):
        self.value = name
        self.personal_id = personal_id

    def __str__(self):
        return f"Сотрудник с именем {self.value} и персональным ИД {self.personal_id} отсутствует в базе"


class AccessErrorOther(MyException):
    def __init__(self):
        pass

    def __str__(self):
        return f"Уровень доступа не достаточен"


if __name__ == '__main__':
    pass
