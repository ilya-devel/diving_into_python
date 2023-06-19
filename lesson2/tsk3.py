BINARY = 2
OCTAL = 8


def get_result(num: int, divider: int):
    result = ""
    while num > 0:
        result = str(num % divider) + result
        num //= divider
    return result


num = None
while True:
    try:
        num = int(input("Введите целое число: "))
        break
    except Exception as err:
        print(err)
        print("Вы ввели не верное значение, попробуйте ещё раз\n")

print(f"{bin(num)} == {get_result(num, BINARY)}")
print(f"{oct(num)} == {get_result(num, OCTAL)}")
