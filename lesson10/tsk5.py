"""
Создайте три (или более) отдельных классов животных.
Например рыбы, птицы и т.п.
У каждого класса должны быть как общие свойства,
например имя, так и специфичные для класса.
Для каждого класса создайте метод, выводящий
информацию специфичную для данного класса.
"""


class Dog:
    def __init__(self, name, worker):
        self.name = name
        self.worker = worker

    def voice(self):
        print("Woof-woof")


class Fish:
    def __init__(self, name, sea):
        self.name = name
        self.sea = sea

    def voice(self):
        print("Бульк-бульк")

    def get_sea(self):
        return self.sea


class Cat:
    def __init__(self, name, family):
        self.name = name
        self.family = family

    def voice(self):
        print("Meow-meow")

    def get_family(self):
        return self.family
