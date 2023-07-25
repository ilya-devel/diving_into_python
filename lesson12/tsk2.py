"""
Доработаем задачу 1.
Создайте менеджер контекста, который при выходе
сохраняет значения в JSON файл.
"""
from tsk1 import Factorial
import json
from datetime import datetime


class FactorialWithManage(Factorial):
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        filename = datetime.now().strftime("%Y-%m-%d_%H-%M-%s")
        with open(f'{filename}.json', 'w', encoding='UTF-8') as f:
            json.dump(self.get_all_result(), f)


if __name__ == '__main__':
    with FactorialWithManage() as fact:
        fact(7)
        fact(3)
