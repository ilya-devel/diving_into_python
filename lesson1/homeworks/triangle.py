triangle = {"A": None, "B": None, "C": None}

for key in triangle.keys():
    while True:
        try:
            triangle[key] = int(input(f"Введите длину стороны {key} треугольника в мм.: "))
            break
        except Exception as err:
            err.__hash__()
            print("Вы ввели неверные данные, попробуйте ещё раз")

a, b, c = triangle.values()

if a + b < c or a + c < b or b + c < a or 0 in triangle.values():
    print("Данные размеры не могут быть у треугольника")
else:
    for key in triangle.keys():
        print(f"Сторона {key} равна {triangle[key]} мм.")
    match len(set(triangle.values())):
        case 1:
            print("Треугольник равносторонний")
        case 2:
            print("Треугольник равнобедренный")
        case _:
            print("Треугольник разносторонний")
