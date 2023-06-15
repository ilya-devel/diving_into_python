height = int(input("Введите высоту ёлки: "))

for i in range(1, height + 1):
    print(f"{' ' * (height - i)}{'*' * (i + (i - 1))}")
