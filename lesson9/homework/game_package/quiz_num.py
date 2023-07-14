"""
Создайте функцию-замыкание, которая запрашивает два целых
числа:
○ от 1 до 100 для загадывания,
○ от 1 до 10 для количества попыток
Функция возвращает функцию, которая через консоль просит
угадать загаданное число за указанное число попыток.
"""


def get_num(max_value=100):
    while True:
        res = input(f'Введите целое число в диапазоне от 1 до {max_value}: ')
        try:
            res = int(res)
            if res < 1 or res > max_value:
                raise Exception(f'Введённое число не входит в диапазон от 1 до {max_value}, попробуйте ещё раз')
        except Exception as err:
            print(f'Введённое значение не является целым числом в диапазоне от 1 до {max_value}, попробуйте ещё раз')
            continue
        return res


def quiz_num_value_with_none(value=None):
    def quiz(quest, attempts):
        while attempts != 0:
            print('Отгадайте число: ')
            ans = get_num(max_value=100)
            if ans == quest:
                return 'Вы угадали'
            if ans > quest:
                print('Не верно, загаданное число меньше')
            else:
                print('Не верно, загаданное число больше')
            attempts -= 1
        return f'Вы проиграли, верный ответ {quest}'

    if value is None:
        print('Введите число для загадывания:')
        value = get_num(max_value=100)

    def quiz_num_attempt(attempt=None):
        if attempt is None:
            print('Введите число количества попыток:')
            attempt = get_num(max_value=10)
        return quiz(value, attempt)

    return quiz_num_attempt


def quiz_num_value(value: int = 100):
    def quiz(quest, attempts):
        while attempts != 0:
            print('Отгадайте число: ')
            ans = get_num(max_value=100)
            if ans == quest:
                return 'Вы угадали'
            if ans > quest:
                print('Не верно, загаданное число меньше')
            else:
                print('Не верно, загаданное число больше')
            attempts -= 1
        return f'Вы проиграли, верный ответ {quest}'

    def quiz_num_attempt(attempt: int = 10):
        return quiz(value, attempt)

    return quiz_num_attempt


if __name__ == '__main__':
    print(quiz_num_value()())
