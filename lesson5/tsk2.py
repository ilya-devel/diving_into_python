"""
Самостоятельно сохраните в переменной строку текста.
Создайте из строки словарь, где ключ — буква, а значение — код буквы.
Напишите преобразование в одну строку.
"""

some_row = "aljkdfk jalkjdf;lajdfajkd;fla"

some_dict = {ch: ord(ch) for ch in some_row}

if __name__ == '__main__':

    for ch, value in some_dict.items():
        print(f"{ch} => {value}")
