def menu():
    print("1.снять деньги")
    print("2.пополнить счет")
    print("3.проверить баланс")
    print("4.история операций")
    print("5.выйти")


class BankAcc:
    def __init__(self, name, acc_num, balance=0):
        self.__balance = balance
        self.name = name
        self.acc_num = acc_num
        self.history = []

    @property
    def balance(self):
        return self.__balance
    
    @balance.setter
    def set_balance(self, value):
        if value < 0:
            print("не может быть отрицательным. ")
        else:
            self.__balance = value

    def add_money(self):
        try:
            add = int(input("Введите сумму пополнения: "))
            if add < 0:
                print("нельзя пополнить")
            else:
                self.__balance += add
                print("бaлaнс пополнен")
                self.history.append(f"сумма пополнения {add}")
                print(f"счет пополнен на {add}")
        except ValueError:
            print("Введите число")

    def take_money(self):
        try:
            take = int(input("Введите сумму:"))
            if take < 0:
                print("cумма не может быть отрицательной")
            elif take > self.__balance:
                print("Недостаточно средств")
            else:
                operations = int(input("Введите количество операций: "))
                commitions = take / operations
                self.__balance -= take
                print("Снято", take)
                print("комисия", commitions)
                self.history.append(f"сумма снятия {take}") 
        except ValueError:
            print("Введите число")
        except ZeroDivisionError:
            print("Количество операций не может быть равно нулю")

        
    def balance_check(self):
        print(f"баланс равен {self.__balance}")


    def history(self):
        for i in self.history:
            print(i)


def main():
    b1 = BankAcc("Igor", 132435, 2000)
    while True:
        menu()
        try:
            num = int(input("Введите цифру команды: "))
            if num == 1:
                b1.take_money()
            elif num ==2:
                b1.add_money()
            elif num == 3:
                b1.balance_check()
            elif num == 4:
                b1.history()
            elif num == 5:
                print("выход")
                break
            else:
                print("Неверный выбор")
        except ValueError:
            print("Введите число а не букву")

if __name__ == "__main__":
    main()