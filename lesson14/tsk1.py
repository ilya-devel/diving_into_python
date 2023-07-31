"""
📌Создайте функцию, которая удаляет из текста все символы
кроме букв латинского алфавита и пробелов.
📌Возвращается строка в нижнем регистре.
"""
import re
import doctest


def clear_text(txt: str) -> str:
    """
    Чистит текст от любых символов и букв, которые не являются латинскими или пробелами
    :param txt:
    :return:
    >>> clear_text("Some text!") == "some text"
    True
    >>> clear_text("Some text!") == "Some text!"
    False
    """
    new_txt = ''
    for ch in txt:
        if re.match(r'[a-zA-Z ]', ch):
            new_txt += ch
    return new_txt.lower()


if __name__ == '__main__':
    doctest.testmod(verbose=True)
