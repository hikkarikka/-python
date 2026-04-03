class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Гав"
    
class Cat(Animal):
    def speak(self):
        return "Мяу"
    
# animals = [Dog(), Cat()]

# for i in animals:
#     print(i.speak())

animal1 = Dog()
animal2 = Cat()

print(animal1.speak())
print(animal2.speak())