# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def bark(self):
#         print("гав")

# dog1 = Dog("Шарик", 3)
# dog2 = Dog("барсик", 2)


# print(dog1.name)
# print(dog1.age)
# print(dog2.name)
# print(dog2.age)

# print(dog1.bark())
# print(dog2.bark())

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    
    def info(self):
        print(f"имя: {self.name}, Оценка: {self.grade}")

s1 = Student("Roman", 85)
s2 = Student("vova", 98)

s1.info
s2.info