"""
Создайте класс-генератор.
Экземпляр класса должен генерировать факториал числа в
диапазоне от start до stop с шагом step.
Если переданы два параметра, считаем step=1.
Если передан один параметр, также считаем start=1.
"""


class FactorialGenerate:
    def __init__(self, *args: int):
        if len(args) == 0:
            raise Exception("InvalidArgument")
        if len(args) == 2:
            start, finish, step = args[0], args[1], 1
        elif len(args) == 1:
            start, finish, step = 1, args[0], 1
        else:
            start, finish, step = args[0], args[1], args[2]
        self.start = start
        self.finish = finish
        self.step = step
        self.result = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.start <= self.finish:
            self.result *= self.start
            self.start += self.step
            return self.result
        raise StopIteration


if __name__ == '__main__':
    for x in FactorialGenerate(1, 5, 1):
        print(x)
    print()
    for x in FactorialGenerate(3, 5):
        print(x)
    print()
    for x in FactorialGenerate(5):
        print(x)

    pass
