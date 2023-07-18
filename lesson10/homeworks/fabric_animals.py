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
        class__ = classes.get(class_name, None)
        if class_ is not None:
            return class__(*args, **kwargs)

        raise Exception("Класс не найден")


if __name__ == '__main__':
    lst_animals = [{'class': 'Cat', 'name': 'Гаф', 'type_animal': 'Сиамская', 'family': 'Бобровы'},
                   {'class': 'Dog', 'name': 'Бобик', 'type_animal': 'Немецкая овчарка', 'worker': 'пограничник'},
                   {'class': 'Horse', 'name': 'Звёздочка', 'type_animal': 'Владимирский тяжеловоз'}]
    for animal in lst_animals:
        try:
            class_ = animal.pop('class')
            show_animal = FabricAnimals.get_class(class_name=class_, **animal)
            print(show_animal)
            print(f"Животное {class_} издаёт звуки: {show_animal.voice()}")
            print()
        except Exception as err:
            print(f"Наша фабрика не занимается данной разновидностью животных ({class_})")
