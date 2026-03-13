# try:
#     # опасный код в котором может быть ошибка
# except название ошибки : #ValueError
#     # сработает код если будет ошибка
# except название ошибки : #ZeroDivisionError
#     # сработает код если будет ошибка
# except Exception:
#     # сработает код если будет ошибка
# else:
#     #код
# finally
#     #код

try:
    num = int(input("Введите число: "))
    print(10 / num)
except ValueError as e:
    print(f"Введите число, сработала ошибка! Описание: {e}")
except ZeroDivisionError as q:
    print(f"Делить на ноль нельзя, описание {q}")
else:
    print("ОШибок нет")
finally:
    print("Код выполнен")