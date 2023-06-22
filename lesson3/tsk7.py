string = input("Введите строку: ")

ver1 = dict()
for s in string:
    if s not in ver1.keys():
        ver1[s] = string.count(s)
print(ver1)

ver2 = dict()
for s in string:
    if s not in ver2.keys():
        ver2[s] = 1
    else:
        ver2[s] += 1
print(ver2)
