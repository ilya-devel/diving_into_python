"""
Добавьте в модуль с загадками функцию, которая хранит словарь списков.
Ключ словаря - загадка, значение - список с отгадками.
Функция в цикле вызывает загадывающую функцию, чтобы передать ей все свои загадки.
"""
from tsk4 import riddle_game


def get_circle_riddles(riddles: dict):
    for question, answers in riddles.items():
        result = riddle_game(question, answers, 3)
        print(f"Вы угадали с {result} попытки\n" if result != 0 else "Вы не угадали\n")


if __name__ == '__main__':
    riddles_ = {
        "Сидит дед в сто шуб одет, кто его раздевает, тот слёзы проливает": ['лук', 'onion'],
        "Висит груша нельзя скушать": ["лампочка", "лампа", "light bulb"]
    }
    get_circle_riddles(riddles_)

