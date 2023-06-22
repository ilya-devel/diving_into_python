from random import randint

lst = [randint(0, 20) for _ in range(20)]

print(lst)

result = []

for i in range(len(lst)):
    if lst[i] % 2 == 1:
        result.append(i + 1)

print(result)
