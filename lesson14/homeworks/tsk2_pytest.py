import pytest
from pathlib import Path
from lesson12.homeworks.student import Student


@pytest.fixture
def path():
    path = Path.cwd() / '..' / '..' / 'lesson12' / 'homeworks' / 'subjects.csv'
    return path


def test_without_file_subjects():
    with pytest.raises(FileNotFoundError):
        assert Student(surname='Black', name='Jack', patronymic='Test')


def test_without_path_to_file_subjects():
    with pytest.raises(ValueError):
        assert Student(surname='Black', name='Jack', patronymic='Test', path_to_file=None)


def test_valid_data(path):
    assert str(Student(surname='Black', name='Jack', patronymic='Test', path_to_file=path)) == 'Black Jack Test'


if __name__ == '__main__':
    pytest.main(['-v'])
