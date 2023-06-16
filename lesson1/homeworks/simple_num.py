num = None
while True:
    try:
        num = int(input("Введите целое значение в диапазоне от 1 до 100000: "))
        if 0 >= num or num > 100_000:
            raise Exception("Число не входит в указанный диапазон!")
        break
    except Exception as err:
        print(err)
        print("Вы ввели не верное значение, попробуйте ещё раз")

msg = None
for i in range(2, num // 2 + 1):
    if num % i == 0:
        msg = "составное"
        break
if msg is None:
    msg = "простое"

print(f"Число {num} {msg}")
