# import math
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
    
#     def distance(self):
#         return math.sqrt(self.x**2 + self.y**2)
    
#     def getPoint(self):
#         return [self.x, self.y]
    
# class PointColor(Point):
#     def __init__(self, x, y, color):
#         super().__init__(x, y)
#         self.color = color

#     def showcolor(self):
#         return self.color
    
# p = Point(4, 7)
# p1 = PointColor(5, 6, "red")
# print(p.getPoint())
# print(p.distance())
# print(p1.showcolor())
# print(p1.getPoint())

class Pet:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def sound(self):
        print("животное издает звук")

    def show(self):
        print(f"имя - {self.name}, возраст - {self.age}, цвет - {self.color}")
        
    def type(self):
        print("Тип: Домашнее животное")

class Dog(Pet):
    def sound(self):
        print("гав")

    def type(self):
        print("Тип собака")

class Cat(Pet):
    def sound(self):
        print("мяу")

    def type(self):
        print("Тип кошка")

class Parrot(Pet):
    def sound(self):
        print("чирик")

    def type(self):
        print("Тип попугай")

class Hamster(Pet):
    def sound(self):
        print("писк")

    def type(self):
        print("Тип хомяк")

dog = Dog("Бобик", 9, "коричневый")
cat = Cat("Муся", 6, "белая")
parrot = Parrot("Коша", 1, "голубой")
hamster = Hamster("Гарик", 3, "серый")

Dog.sound(Pet)
Cat.sound(Pet)
Parrot.sound(Pet)
Hamster.sound(Pet)