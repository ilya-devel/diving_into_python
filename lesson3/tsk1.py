from random import randint


def long_method(lst_tmp: list):
    result = []
    for num in lst_tmp:
        if num not in result:
            result.append(num)
    return sorted(result)


lst = [randint(0, 20) for _ in range(20)]

print(f"Main list: {lst}")
print(f"Fast method: {list(set(lst))}")
print(f"Long method: {long_method(lst)}")
