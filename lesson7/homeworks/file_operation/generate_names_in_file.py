"""
✔ Напишите функцию, которая генерирует
псевдоимена.
✔ Имя должно начинаться с заглавной буквы,
состоять из 4-7 букв, среди которых
обязательно должны быть гласные.
✔ Полученные имена сохраните в файл.
"""

from os import sep
from pathlib import Path
from random import randint, choice


def name_generate(file_name='tsk2_data.txt'):
    some_path = Path.cwd() / 'some_data'
    Path(some_path).mkdir(parents=True, exist_ok=True)
    vowels = 'aeiyuo'
    consonants = 'qwrtpsdfghjklzxcvbnm'
    with open(f'{some_path}{sep}{file_name}', 'a', encoding='UTF-8') as f:
        some_name = ''.join([choice([choice(vowels), choice(consonants)]) for _ in range(randint(4, 7))])
        print(some_name.capitalize(), file=f)


if __name__ == '__main__':
    name_generate('tsk2_data.txt')
