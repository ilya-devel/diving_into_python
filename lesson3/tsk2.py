lst = [string.strip() for string in input("Введите разные данные через запятую: ").split(",")]

for i in range(len(lst)):
    tmp = lst[i]
    if tmp.isdigit():
        lst[i] = int(tmp)
    elif "." in tmp and False not in set([t.isdigit for t in tmp.split('.')]):
        lst[i] = float(tmp)
    elif True in [t.upper() == t for t in tmp]:
        lst[i] = tmp.lower()
    else:
        lst[i] = tmp.upper()

print(lst)
