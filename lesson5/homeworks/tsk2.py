"""
Напишите однострочный генератор словаря, который принимает
на вход три списка одинаковой длины: имена str, ставка int,
премия str с указанием процентов вида «10.25%». В результате
получаем словарь с именем в качестве ключа и суммой
премии в качестве значения. Сумма рассчитывается
как ставка умноженная на процент премии
"""
from decimal import Decimal

lst_names = ["mike", "roza", "maria"]
lst_salaries = [1000, 1250, 800]
lst_awards = ["10.2%", "5.1%", "15.7%"]

some_dict = {name: (salary * Decimal(award.replace("%", ""))) for name, salary, award in
             zip(lst_names, lst_salaries, lst_awards)}

for some_name, bonus in some_dict.items():
    print(f"{some_name} => {bonus}")
