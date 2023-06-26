"""
Напишите функцию, которая принимает строку текста.
Вывести функцией каждое слово с новой строки.
Строки нумеруются начиная с единицы.
Слова выводятся отсортированными согласно кодировки Unicode.
Текст выравнивается по правому краю так, чтобы у самого
длинного слова был один пробел между ним и номером строки.
"""


def show_list_word(row: str) -> list:
    lst = sorted([word.strip() for word in row.split()])
    for i in range(len(lst)):
        print(f"{i+1:3d} {lst[i]:>{max(map(len, lst))}}")


show_list_word("Напишите функцию, которая принимает строку текста")
