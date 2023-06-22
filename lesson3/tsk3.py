lst = (1, 3.2, "str", [1, 2], 4)

result = dict()
for i in lst:
    key = str(type(i))
    if key not in result.keys():
        result[key] = []
    result[key].append(i)

for key in result.keys():
    print(f"{key} == {result[key]}")
