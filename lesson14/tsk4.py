"""
📌Напишите для задачи 1 тесты pytest. Проверьте следующие
варианты:
📌возврат строки без изменений
📌возврат строки с преобразованием регистра без потери
символов
📌возврат строки с удалением знаков пунктуации
📌возврат строки с удалением букв других алфавитов
📌возврат строки с учётом всех вышеперечисленных пунктов
(кроме п. 1)
"""

from lesson14.tsk1 import clear_text
import pytest


def test_no_change():
    assert clear_text('some text') == 'some text'


def test_method_second():
    assert clear_text('Some text') == 'some text'


def test_method_third():
    assert clear_text('some, text') == 'some text'


def test_method_fourth():
    assert clear_text('Наверное:some text') == 'some text'


def test_method_five():
    assert clear_text('SoМme text!') == 'some text'


if __name__ == '__main__':
    pytest.main()
