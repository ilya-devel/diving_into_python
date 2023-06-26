"""
Создайте несколько переменных заканчивающихся и не оканчивающихся на «s».
Напишите функцию, которая при запуске заменяет содержимое переменных оканчивающихся на s (кроме переменной из одной буквы s) на None.
Значения не удаляются, а помещаются в одноимённые переменные без s на конце.
"""


def change_variables(lst_var):
    for key in lst_var:
        if key == "s":
            continue
        if key.endswith("s"):
            tmp_key = key[:-1]
            if tmp_key in lst_var:
                tmp = globals()[key]
                globals()[tmp_key] = tmp
                globals()[key] = None


s = 1
socks = 3
sock = None
gift = 6

change_variables(globals().keys())

print(f"{s = }")
print(f"{socks = }")
print(f"{sock = }")
