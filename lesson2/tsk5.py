print(f"Формула A*x^2 + B*x + C = 0, введите данные для A,B,C:")
argument = {"A": None, "B": None, "C": None}

for key in argument.keys():
    while True:
        try:
            argument[key] = int(input(f"Введите значение {key}: "))
            break
        except Exception as err:
            print("Вы ввели неверные данные, попробуйте ещё раз")

a, b, c = argument.values()

d = (b ** 2) - (4 * a * c)

if d < 0:
    d = complex((b ** 2) - (4 * a * c))
    print(f"Комплексный корень X1 = {(-b + d ** 0.5) / 2 * a}")
    print(f"Комплексный корень X2 = {(-b - d ** 0.5) / 2 * a}")
elif d == 0:
    print(f"X = {-b / 2 * a}")
else:
    print(f"Корень X1 = {(-b + d ** 0.5) / 2 * a}")
    print(f"Корень X2 = {(-b - d ** 0.5) / 2 * a}")
