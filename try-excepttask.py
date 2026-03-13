def menu():
    print("1.снять деньги")
    print("2.пополнить счет")
    print("3.проверить баланс")
    print("4.выйти")

def take_money(balance):
    try:
        take = int(input("Введите сумму:"))
        if take < 0:
            print("cумма не может быть отрицательной")
        elif take > balance:
            print("Недостаточно средств")
        else:
            operations = int(input("Введите количество операций: "))
            commitions = take / operations
            balance -= take
            print("Снято", take)
            print("комисия", commitions)
    except ValueError:
        print("Введите число")
    except ZeroDivisionError:
        print("Количество операций не может быть равно нулю")
    else:
        print("Операция выполнена успешно")
    finally:
        print("операция завершена")
    return balance

def add_money(balance):
    try:
        add = int(input("Введите сумму пополнения: "))
        if add < 0:
            print("нельзя пополнить")
        else:
            balance += add
            print("бвлвнс пополнен")
    except ValueError:
        print("Введите число")
    finally:
        print("Операция завершена")
    return balance

def balance_check(balance):
    print(balance)


def main():
    balance = 5000
    while True:
        menu()
        try:
            num = int(input("Введите цифру команды: "))
            if num == 1:
                balance = take_money(balance)
            elif num ==2:
                balance = add_money(balance)
            elif num == 3:
                balance_check(balance)
            elif num == 4:
                break
            else:
                print("Неверный выбор")
        except ValueError:
            print("Введите число а не букву")



if __name__ == "__main__":
    main()