"""
Доработайте задачу 5.
Вынесите общие свойства и методы классов в класс
Животное.
Остальные классы наследуйте от него.
Убедитесь, что в созданные ранее классы внесены правки.
"""


class Animal:
    def __init__(self, name):
        self.name = name

    def voice(self):
        pass


class Dog(Animal):
    def __init__(self, worker, *args, **kwargs):
        self.worker = worker
        super().__init__(*args, **kwargs)

    def voice(self):
        print("Woof-woof")

    def get_worker(self):
        return self.worker


class Fish(Animal):
    def __init__(self, sea, *args, **kwargs):
        self.sea = sea
        super().__init__(*args, **kwargs)

    def voice(self):
        print("Бульк-бульк")

    def get_sea(self):
        return self.sea


class Cat(Animal):
    def __init__(self, family, *args, **kwargs):
        self.family = family
        super().__init__(*args, **kwargs)

    def voice(self):
        print("Meow-meow")

    def get_family(self):
        return self.family


if __name__ == '__main__':
    cat = Cat(name='Gaf', family='Bobrovi')
    dog = Dog(name='Arrow', worker='hunter dog')
    fish = Fish(name='Goldy', sea='Black sea')
    for animal in [cat, dog, fish]:
        animal.voice()
    print(cat.get_family())
    print(dog.get_worker())
    print(fish.get_sea())
