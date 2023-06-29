def my_fibonacci(length: int, pos1=0, pos2=1):
    nums = [pos1, pos2]
    for _ in range(length):
        nums.append(sum(nums))
        yield nums.pop(0)


def my_factorial(length: int):
    num = 1
    for i in range(1, length + 1):
        num *= i
        yield num


for n in my_fibonacci(10, pos1=2, pos2=3):
    print(n)

for ind, value in enumerate(my_factorial(10), start=1):
    print(f"{ind} => {value}")

print(my_fibonacci(10))
print(my_fibonacci(100))
