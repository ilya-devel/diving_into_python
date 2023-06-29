"""
Продолжаем развивать задачу 2.
Возьмите словарь, который вы получили.
Сохраните его итератор.
Далее выведите первые 5 пар ключ-значение,
обращаясь к итератору, а не к словарю.
"""

from tsk2 import some_dict

some_iter = iter(some_dict.items())

for _ in range(5):
    key, value = next(some_iter)
    print(f"{key} => {value}")
