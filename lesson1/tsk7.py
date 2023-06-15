msg = None
result = None
while True:
    num = int(input(f"{msg}Введите число от 1 до 999: "))
    if 1 <= num <= 999:
        if num < 10:
            result = num ** 2
        elif 10 <= num <= 99:
            result = (num // 10 * 10) - (num % 10)
        elif 100 <= num <= 999:
            result = (num % 10 * 100) + (num % 100 // 10 * 10) + (num // 100)
        break
    else:
        msg = "Вы ввели не верное число, попробуйте ещё раз\n"
        continue

print(result)
