from menu import menu
from acc import BankAcc

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
                b1.check_history()
            elif num == 5:
                print("выход")
                break
            else:
                print("Неверный выбор")
        except ValueError:
            print("Введите число а не букву")

if __name__ == "__main__":
    main()