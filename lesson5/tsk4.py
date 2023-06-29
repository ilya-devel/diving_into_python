"""
Создайте генератор чётных чисел от нуля до 100.
Из последовательности исключите
числа, сумма цифр которых равна 8.
Решение в одну строку.
"""

# some_generator = (i for i in range(101) if sum(map(int, str(i))) != 8 and i % 2 == 0)
some_generator = (i for i in range(0, 101, 2) if sum(map(int, str(i))) != 8)

for value in some_generator:
    print(value)
