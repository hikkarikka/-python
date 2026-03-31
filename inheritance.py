# class Animal:
#     def speak(self):
#         print("животное издает звук")

# class Dog(Animal):
#     pass

# dog = Dog()
# dog.speak()

# Override - переопределение метода

# class Animal:
#     def speak(self):
#         print("животное издает звук")

# class Dog(Animal):
#     def speak(self):
#         print("Гав")

# dog = Dog()
# dog.speak()

# про super().название метода()
class Animal:
    def __init__(self, name):
        self.name = name
    # def speak(self):
    #     print("звук")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    # def speak(self):
    #     super().speak()
    #     print("гав")

dog = Dog("bobik", "husky")