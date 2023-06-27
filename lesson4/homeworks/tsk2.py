"""
Напишите функцию принимающую на вход только ключевые
параметры и возвращающую словарь, где ключ — значение
переданного аргумента, а значение — имя аргумента. Если
ключ не хешируем, используйте его строковое представление.
"""


def some_function(**kwargs):
    some_dict = dict()
    for some_key, some_value in kwargs.items():
        some_dict[some_value] = some_key
    return some_dict


if __name__ == '__main__':
    for key, value in some_function(var1=1, var2='ajdlf', var3=2.4, var4="alkjdf").items():
        print(f'{key} => {value}')
