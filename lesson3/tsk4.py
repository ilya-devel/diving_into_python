from random import randint

lst = [randint(0, 20) for _ in range(20)]

print(lst)

new_lst = []
for i in lst:
    if lst.count(i) != 2:
        new_lst.append(i)

print(new_lst)
