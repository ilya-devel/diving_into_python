"""
Функция принимает на вход три списка одинаковой длины:
имена str,
ставка int,
премия str с указанием процентов вида «10.25%».
Вернуть словарь с именем в качестве ключа и суммой
премии в качестве значения.
Сумма рассчитывается как ставка умноженная на процент премии.
"""
from decimal import Decimal


def get_dict_award(lst_name, lst_salary, lst_award):
    tmp_dict = dict()
    for name_, salary, award_ in zip(lst_name, lst_salary, lst_award):
        tmp_dict[name_] = salary * Decimal(award_.replace("%", ""))
    return tmp_dict


lst_names = ["mike", "roza", "maria"]
lst_salaries = [1000, 1250, 800]
lst_awards = ["10.2%", "5.1%", "15.7%"]

for name, award in get_dict_award(lst_names, lst_salaries, lst_awards).items():
    print(f"{name} => {award}")
