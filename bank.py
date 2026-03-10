class BankAcc:
    def __init__(self, name, balance, acc_num):
        self.name = name
        self._balance = balance
        self.__acc_num = acc_num

    @property
    def balance(self):
        return self._balance
    
    @balance.setter
    def balance(self, balance):
        if balance <= 0:
            print("невозможно изменить баланс")
        else:
            self._balance = balance
    
    @property
    def acc_num(self):
        return self.__acc_num
    
    @acc_num.setter
    def acc_num(self, new_acc):
        self.__acc_num = new_acc
    
    def deposit(self, sum):
        if sum > 0:
            self._balance += sum
            print("баланс пополнен")
        else:
            print("сумма должна быть больше нуля")

    def take_money(self, sum):
        if sum > self._balance:
            print("недостаточно средств")
        elif sum <= 0:
            print("неправильная сумма")
        else:
            self._balance -= sum
            print("деньги сняты")

    def get_info(self):
        print(self.name)
        print(self._balance)
        print(self.__acc_num)

b1 = BankAcc("Alex", 5000 , 121223)
# b1.set_balance(4700)
# print(b1.get_balance())
b1.get_info()

print(b1.acc_num)
b1.acc_num = 131323
print(b1.acc_num)