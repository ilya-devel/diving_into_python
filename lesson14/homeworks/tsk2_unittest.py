import unittest
from pathlib import Path
from lesson12.homeworks.student import Student


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.path = Path.cwd() / '..' / '..' / 'lesson12' / 'homeworks' / 'subjects.csv'

    def test_without_file_subjects(self):
        self.assertRaises(FileNotFoundError, Student, surname='Black', name='Jack', patronymic='Test')

    def test_without_path_to_file_subjects(self):
        self.assertRaises(ValueError, Student, surname='Black', name='Jack', patronymic='Test', path_to_file=None)

    def test_valid_data(self):
        self.assertEqual(str(Student(surname='Black', name='Jack', patronymic='Test', path_to_file=self.path)),
                         'Black Jack Test')


if __name__ == '__main__':
    unittest.main()
