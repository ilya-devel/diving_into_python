"""
Вспомните какие модули вы уже проходили на курсе.
Создайте файл, в котором вы импортируете встроенные в модуль функции под псевдонимами. (3-7 строк импорта).
"""
from os import sep as s
import sys
from random import randint
import datetime
import math
from itertools import combinations as comb

if __name__ == '__main__':
    print(f"{s = }")
    print(sys.argv)
    print(f"{randint(1, 100) = }")
    print(datetime.datetime.now())
    print(math.pi)
    print(list(comb([1, 2, 3, 4], 2)))
