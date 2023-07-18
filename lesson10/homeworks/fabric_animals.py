"""
Доработаем задачи 5-6. Создайте класс-фабрику.
○ Класс принимает тип животного (название одного из созданных классов)
и параметры для этого типа.
○ Внутри класса создайте экземпляр на основе переданного типа и
верните его из класса-фабрики.
"""
from animals import Animal


class FabricAnimals:
    @staticmethod
    def get_class(class_name: str, *args, **kwargs) -> object:
        if type(class_name) != str:
            raise ValueError("class_name должен быть строкой")

        raw_classes_ = Animal.__subclasses__()
        classes = {c.__name__: c for c in raw_classes_}
        class_ = classes.get(class_name, None)
        if class_ is not None:
            return class_(*args, **kwargs)

        raise Exception("Класс не найден")


if __name__ == '__main__':
    lst_animals = ['Cat', 'Dog', 'Horse']
    for animal in lst_animals:
        # show_animal = FabricAnimals().get_class(animal)
        # print(show_animal.voice())
        try:
            show_animal = FabricAnimals.get_class(animal)
            print(f"Животное {animal} издаёт звуки: {show_animal.voice()}")
        except Exception as err:
            print(f"Наша фабрика не занимается данной разновидностью животных ({animal})")
