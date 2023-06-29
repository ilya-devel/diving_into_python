"""
Создайте функцию генератор чисел Фибоначчи (см. Википедию).
"""


def my_fibonacci(length: int, pos1=0, pos2=1):
    nums = [pos1, pos2]
    for _ in range(length):
        nums.append(sum(nums))
        yield nums.pop(0)


for n in my_fibonacci(10):
    print(n)
