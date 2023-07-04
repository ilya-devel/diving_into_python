"""
Создайте модуль с функцией внутри.
Функция принимает на вход три целых числа: нижнюю и верхнюю границу и количество попыток.
Внутри генерируется случайное число в указанных границах и пользователь должен угадать его за заданное число попыток.
Функция выводит подсказки “больше” и “меньше”.
Если число угадано, возвращается истина, а если попытки исчерпаны - ложь.
"""

from random import randint


def guess_game(min_=1, max_=10, attempts=3):
    some_num = randint(min_, max_)
    while attempts != 0:
        try:
            guess = int(input("Введите предпологаемое число: "))
            if guess == some_num:
                print("Вы угадали")
                break
            elif guess < some_num:
                print("Число больше")
            else:
                print("Число меньше")
        except Exception as err:
            print("Вы потеряли попытку, т.к. не корректно ввели число!")
        finally:
            attempts -= 1
    else:
        print(f"Вы проиграли, правильный ответ: {some_num}")


def guess_game2(min_=1, max_=100, attempts=5):
    some_num = randint(min_, max_)
    while attempts != 0:
        try:
            guess = int(input("Введите предпологаемое число: "))
            if guess == some_num:
                print("Вы угадали")
                break
            elif guess < some_num:
                print("Число больше")
            else:
                print("Число меньше")
        except Exception as err:
            print("Вы потеряли попытку, т.к. не корректно ввели число!")
        finally:
            attempts -= 1
    else:
        print(f"Вы проиграли, правильный ответ: {some_num}")


if __name__ == '__main__':
    guess_game(1, 10, 3)
