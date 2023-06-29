"""
✔ Создайте функцию-генератор.
✔ Функция генерирует N простых чисел,
начиная с числа 2.
✔ Для проверки числа на простоту используйте
правило: «число является простым, если делится
нацело только на единицу и на себя».
"""


def some_generator():
    for i in range(2, 10000):
        check = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                check = False
                break
        if check:
            yield i


some_generator2 = (i for i in range(2, 100) if False not in (False for j in range(2, int(i ** 0.5) + 1) if i % j == 0))

for val in some_generator2:
    print(val)
