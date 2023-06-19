num: int = 3
fraction: float = 5.8
name: str = "Laze"
ans: bool = True
dictionary: dict = {'one': 1, 'two': 2}
lst: list = [1, "2", 3]
tupl: tuple = (1, 2, 3)
set_: set = {1, 2, 3}
fr: frozenset = frozenset([1, 2, 3])

for t in [num, fraction, name, ans, dictionary, lst, tupl, set_, fr]:
    print(f"{t} is {type(t)}")

fr = fr.union({4})

print(fr)
