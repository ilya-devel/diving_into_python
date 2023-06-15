FOUR = 4
HUNDRED = 100
FOUR_HUNDRED = 400
GREGORY = 1582

check_year = int(input("Введите год для проверки: "))

if check_year < GREGORY:
    print("На тот момент не было календаря")
else:
    if check_year % FOUR == 0:
        if check_year % HUNDRED == 0:
            if check_year % FOUR_HUNDRED == 0:
                print("Год високосный")
            else:
                print("Год не високосный")
        else:
            print("Год високосный")
    else:
        print("Год не високосный")

if check_year < GREGORY:
    print("На тот момент не было календаря")
elif check_year % FOUR == 0 and check_year % HUNDRED == 0 and check_year % FOUR_HUNDRED == 0:
    print("Год високосный")

# print("Год високосный")
# print("Год не високосный")
