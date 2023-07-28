"""
Создайте функцию, которая запрашивает числовые данные от
пользователя до тех пор, пока он не введёт целое или
вещественное число.
Обрабатывайте не числовые данные как исключения.
"""


def get_number():
    while True:
        try:
            num = float(input("Введите целое или вещественное число: "))
            break
        except Exception as err:
            print(f"{err}. Try again.")
    return num


if __name__ == '__main__':
    print(get_number())
