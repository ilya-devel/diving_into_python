"""
Создайте класс студента.
○ Используя дескрипторы проверяйте ФИО на первую заглавную букву и
наличие только букв.
○ Названия предметов должны загружаться из файла CSV при создании
экземпляра. Другие предметы в экземпляре недопустимы.
○ Для каждого предмета можно хранить оценки (от 2 до 5) и результаты
тестов (от 0 до 100).
○ Также экземпляр должен сообщать средний балл по тестам для каждого
предмета и по оценкам всех предметов вместе взятых.
"""
from pprint import pprint
from pathlib import Path
from random import randint

from descriptors import CheckName, GetListSubjects, Range

LST_SUBJECTS = Path.cwd() / 'subjects.csv'


class Grade:
    __slots__ = ['grade']

    def __init__(self, grade=None):
        self.grade = grade

    def __str__(self):
        return f"{self.grade}"

    def __repr__(self):
        return f"Grade(grade={self.grade})"


class GradeForTest(Grade):
    grade = Range(1, 100)


class GradeForSubject(Grade):
    grade = Range(2, 5)


class Student:
    """
    Класс представляет форму для заполнения данных об успеваемости студента
    """
    surname = CheckName()
    name = CheckName()
    patronymic = CheckName()
    subjects = GetListSubjects()

    def __init__(self, surname=None, name=None, patronymic=None, path_to_file=LST_SUBJECTS):
        """
        Создаёт экземпляр класс, заполняя ФИО студента и создав пустой список оценок по предметам для заполнения
        :param surname: фамилия
        :param name: имя
        :param patronymic: отчество
        :param path_to_file: путь к файлу со списком предметов
        """
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.subjects: dict = path_to_file

    def __str__(self):
        return f'{self.surname} {self.name} {self.patronymic}'

    def __repr__(self):
        return f'Student(surname={self.surname}, name={self.name}, patronymic={self.patronymic})\n' \
               f'{self.subjects}'

    def add_grade(self, subject_, grade, test=True):
        """
        Добавляет оценку студенту
        :param subject_: имя предмета из списка
        :param grade: оценка
        :param test: оценка за тест (True) или по предмету (False)
        :return:
        """
        if subject_ not in self.subjects.keys():
            raise KeyError("Данного предмета нет в списках")
        if test:
            self.subjects[subject_]['test_values'].append(GradeForTest(grade))
        else:
            self.subjects[subject_]['subject_value'] = GradeForSubject(grade)

    def get_gpa(self, subject_name=None):
        """
        Возвращает средний бал студента за тесты по предмету в зависимости от переданных параметров
        :param subject_name: если указан предмет, вернёт средний бал по тестам иначе среднюю оценку за все предметы
        :return:
        """
        if subject_name is None:
            res = sum([self.subjects[key]['subject_value'].grade for key in self.subjects.keys()]) / len(
                self.subjects.keys())
            return f"Средний бал по всем предметам: {res}"
        if subject_name is not None:
            lst_values = self.subjects[subject_name]['test_values']
            res = sum(map(lambda x: x.grade, lst_values)) / len(lst_values)
            return f"Средний бал за тесты по предмету {subject_name} равен: {res: 0.2f}"


if __name__ == '__main__':
    students = []
    fullnames = ['Ахметзянов Ильяс Альфатович', 'ахметзянова иля альфатовна', 'Метаморф1 666 вер2', '']
    for fn in fullnames:
        surname_, name_, patronymic_ = fn.split() if fn else ['', '', '']
        try:
            students.append(Student(surname=surname_,
                                    name=name_,
                                    patronymic=patronymic_,
                                    ))
        except Exception as err:
            print(err)
    pprint(students)
    print()
    # Заполняем случайными данными
    if len(students) > 0:
        student = students[0]
        for subject in student.subjects.keys():
            for _ in range(randint(10, 20)):
                student.add_grade(subject, randint(57, 100))
            student.add_grade(subject, randint(2, 5), False)

        print(student.get_gpa())
        print(student.get_gpa('math'))
