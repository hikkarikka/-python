# "r" - режим чтения
# "w" - режим записи
# "a" - режим добавления в конец
# "x" - создать новый файл
# "b" - бинарный режим
# "t" - текстовый

# file = open("test.txt", "a")
# text = file.write("1234556543\n")
# file.close()

# file = open("test.txt", "r")
# text = file.read()
# for line in file:
#     print(line)
# file.close()

# with open("test.txt", "r") as file:
#     text = file.read()
#     print(text)

numbers = ["яблоко", "банан"]

# with open("test.txt", "w", encoding="UTF-8") as file:
#     for num in numbers:
#         file.write(str(num) + "\n")

# with open("test.txt", "w") as file:
#     numbers = file.readlines()

# print(numbers[3])

#########################
#работа с json
##########################
import json

user = {
    "name" : "Alex",
    "age" : "20",
    "gender" : "M"
}

with open("user.json", "w") as file:
    json.dump(user, file, indent=4)

with open("user.json", "r") as file:
    data= json.load(file)

print(data)