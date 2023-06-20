"""
Напишите программу, которая принимает две строки
вида “a/b” — дробь с числителем и знаменателем.
Программа должна возвращать сумму
и *произведение дробей. Для проверки своего
кода используйте модуль fractions
"""
from fractions import Fraction


def get_fractions():
    val = {"main": None, "whole": None, "natural": None}
    while True:
        try:
            tmp = input("Введите дробное число через \"/\": ")
            val["whole"], val["natural"] = [int(i.strip()) for i in tmp.split("/")]
            if 0 in val.values():
                raise Exception("Не верно указано число")
            break
        except Exception as err:
            print(err)
            print("Вы ввели не верное значение, попробуйте ещё раз\n")
    print()
    return val


def get_less_value(frac):
    for i in range(frac["whole"], 1, -1):
        if frac["whole"] % i == 0 and frac["natural"] % i == 0:
            frac["whole"] //= i
            frac["natural"] //= i
            break
    return frac


def get_main_fractal(frac):
    if frac["whole"] // frac["natural"] > 0:
        frac["main"] = frac["whole"] // frac["natural"]
        frac["whole"] = frac["whole"] % frac["natural"]
    return frac


def add_fractions(frac1, frac2):
    frac = frac1.copy()
    if frac1["natural"] == frac2["natural"]:
        frac["whole"] += frac2["whole"]
    else:
        frac = add_fractions(
            {"main": None, "whole": frac1["whole"] * frac2["natural"], "natural": frac1["natural"] * frac2["natural"]},
            {"main": None, "whole": frac2["whole"] * frac1["natural"], "natural": frac1["natural"] * frac2["natural"]})
    frac = get_main_fractal(frac)
    frac = get_less_value(frac)
    return frac


def mult_fractions(frac1, frac2):
    frac = frac1.copy()
    frac["whole"] *= frac2["whole"]
    frac["natural"] *= frac2["natural"]
    frac = get_main_fractal(frac)
    frac = get_less_value(frac)
    return frac


fractals = []
for _ in range(2):
    fractals.append(get_fractions())

add_res = add_fractions(fractals[0], fractals[1])
check_add = Fraction(f"{fractals[0]['whole']}/{fractals[0]['natural']}") + Fraction(
    f"{fractals[1]['whole']}/{fractals[1]['natural']}")

print(
    f"Сумма дробей {fractals[0]['whole']}/{fractals[0]['natural']} & {fractals[1]['whole']}/{fractals[1]['natural']} \
равна: {str(add_res['main']) + '*' if add_res['main'] is not None else ''}{add_res['whole']}/{add_res['natural']}  \
(Верный ответ: {check_add})")

mult_res = mult_fractions(fractals[0], fractals[1])
check_mult = Fraction(f"{fractals[0]['whole']}/{fractals[0]['natural']}") * Fraction(
    f"{fractals[1]['whole']}/{fractals[1]['natural']}")

print(
    f"Произведение дробей {fractals[0]['whole']}/{fractals[0]['natural']} & {fractals[1]['whole']}/\
{fractals[1]['natural']} равна: {str(mult_res['main']) + '*' if mult_res['main'] is not None else ''}\
{mult_res['whole']}/{mult_res['natural']}  (Верный ответ: {check_mult})")
