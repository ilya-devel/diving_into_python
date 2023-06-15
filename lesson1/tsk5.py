n = 101
s = 0
i = 0
e = 3
# while i < n:
#     i += 1
#     if i % e == 0 or i % 2 != 0:
#         continue
#     s += i

# while i < n:
#     i += 1
#     if i % e == 0:
#         continue
#     if i % 2 == 0:
#          s += i

# for i in range(n):
#     if i % e == 0 or i % 2 != 0:
#         continue
#     s += i

for i in range(0, n, 2):
    if i % e == 0:
        continue
    s += i

print(s)
