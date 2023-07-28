"""
Создайте функцию аналог get для словаря.
Помимо самого словаря функция принимает ключ и
значение по умолчанию.
При обращении к несуществующему ключу функция должна
возвращать дефолтное значение.
Реализуйте работу через обработку исключений.
"""


def get_value_from_dict(some_dict: dict, key: str, default_value: object):
    try:
        return some_dict[key]
    except Exception as err:
        print(f"{err}. Добавляем значение по умолчанию")
        some_dict[key] = default_value
        return some_dict[key]


if __name__ == '__main__':
    tmp = {'1': 1, '2': '2'}
    print(get_value_from_dict(tmp, key='3', default_value=3))
    print(get_value_from_dict(tmp, key='2', default_value=3))
    print(tmp)
