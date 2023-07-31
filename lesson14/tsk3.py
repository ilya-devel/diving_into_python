"""
📌Напишите для задачи 1 тесты unittest. Проверьте
следующие варианты:
📌возврат строки без изменений
📌возврат строки с преобразованием регистра без потери
символов
📌возврат строки с удалением знаков пунктуации
📌возврат строки с удалением букв других алфавитов
📌возврат строки с учётом всех вышеперечисленных пунктов
(кроме п. 1)
"""

import unittest
from tsk1 import clear_text


class TestClearText(unittest.TestCase):
    def test_method_first(self):
        self.assertTrue(clear_text('some text'), 'some text')

    def test_method_second(self):
        self.assertTrue(clear_text('Some text'), 'some text')

    def test_method_third(self):
        self.assertTrue(clear_text('some, text'), 'some text')

    def test_method_fourth(self):
        self.assertTrue(clear_text('Наверное:some text'), 'some text')

    def test_method_five(self):
        self.assertTrue(clear_text('SoМme text!'), 'some text')


if __name__ == '__main__':
    unittest.main()
