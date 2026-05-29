

# name = input("Ведите свое имя: ")

# def hello(name):
#     with open("user.txt", "a", encoding="UTF-8") as file:
#         file.write(name + "\n")
#     with open("user.txt", "r", encoding="UTF-8") as file:
#         text = file.readlines()
#         for name in text:
#             print(f"Привет {name}")

# hello(name)

# def lines():
#     with open("user.txt", "r", encoding="UTF-8") as file:
#         text = file.readlines()
#         line = len(text)
#         print(line)

# lines()

def words():
    with open("user.txt", "r", encoding="UTF-8") as file:
        text = file.read()
        word = text.split()
        print(len(word))

words()