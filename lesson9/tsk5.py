"""
Объедините функции из прошлых задач.
Функцию угадайку задекорируйте:
○ декораторами для сохранения параметров,
○ декоратором контроля значений и
○ декоратором для многократного запуска.
Выберите верный порядок декораторов.
"""
from tsk1 import get_num
from tsk3 import write_json
from tsk2 import check_values
from tsk4 import loop


@loop(3)
@write_json
@check_values
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


if __name__ == '__main__':
    print(quiz(1, 1))
