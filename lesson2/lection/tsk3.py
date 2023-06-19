text = input("Введите текст: ")

if text.isnumeric():
    print(bin(int(text)))
    print(oct(int(text)))
    print(hex(int(text)))
else:
    print("Текст не число")
    if text.isascii():
        print("Текст написан в ASCII")
    else:
        print("Текст не написан в ASCII")
