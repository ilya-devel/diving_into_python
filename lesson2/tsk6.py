class Atm:
    PERCENT_PUT = 3
    PERCENT_TAKE = 1.5
    TAX = 10

    def __init__(self):
        self.account = 0.0
        self.count = 0

    def get_info(self):
        print(f"На счёте {self.account}")

    def put_money(self, value):
        self.check_account()
        if not value % 50 == 0:
            raise Exception("Сумма не кратна 50")
        self.account += value
        print(f"На счёт положена сумма: {value}")
        self.count += 1
        self.take_perc()

    def take_money(self, value):
        self.check_account()
        perc = value / 100 * Atm.PERCENT_TAKE
        if perc < 30:
            perc = 30
        if perc > 600:
            perc = 600
        if value + perc > self.account:
            raise Exception("Сумма для снятие с комиссией превышает сумму счёта")
        self.account -= value + perc
        print(f"Со счёта снята сумма: {value}")
        self.count += 1
        self.take_perc()

    def take_perc(self):
        if self.count % 3 == 0 and self.count != 0:
            self.account += self.account / 100 * Atm.PERCENT_PUT
            self.count = 0
        print(f"Текущая сумма на счёте: {self.account}")

    def check_account(self):
        if self.account > 5_000_000:
            self.account -= self.account / 100 * Atm.TAX
            print("Снят налог на богатство")


def get_value():
    val = None
    while True:
        try:
            val = float(input("Введите сумму: "))
            if val <= 0:
                raise Exception("Не верно указана сумма")
            break
        except Exception as err:
            print(err)
            print("Вы ввели не верное значение, попробуйте ещё раз\n")
    return val


account = Atm()

while True:
    print("""
    1. Положить деньги на счёт
    2. Снять деньги со счёта
    3. Получить информацию о счёте
    0. Уйти
    """)
    choice = input("Выберите операцию: ")
    try:
        match choice:
            case "1":
                value = get_value()
                account.put_money(value)
            case "2":
                value = get_value()
                account.take_money(value)
            case "3":
                account.get_info()
            case "0":
                break
            case _:
                print("Такого пункта нет")
    except Exception as err:
        print(err)
        print("Попробуйте ещё раз")
