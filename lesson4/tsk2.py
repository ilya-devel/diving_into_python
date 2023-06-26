"""
Напишите функцию, которая принимает строку текста.
Сформируйте список с уникальными кодами Unicode каждого
символа введённой строки отсортированный по убыванию.
"""


def get_code_unicode(row: str):
    lst = []
    for ch in row:
        lst.append(ord(ch))
    return sorted(set(lst), reverse=True)


for code in get_code_unicode("This is testing row"):
    print(code)
