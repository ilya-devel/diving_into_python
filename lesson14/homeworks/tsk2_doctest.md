    >>> from lesson12.homeworks.student import Student
    >>> from lesson12.homeworks.descriptors import CheckName, GetListSubjects, Range
    >>> from pathlib import Path
    >>> path = Path.cwd()/'..'/'..'/'lesson12'/'homeworks'/'subjects.csv'

    >>> print(Student(surname='Black', name='Jack', patronymic='Test', path_to_file=path))
    Black Jack Test

    >>> print(Student(surname='black', name='Jack', patronymic='Test', path_to_file=path))
    Traceback (most recent call last):
      ...
    ValueError: Значение black должно начинаться с заглавной буквы

