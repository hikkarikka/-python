# class Circle:
#     def __init__(self, radius):
#         self.radius = radius

#     def __add__(self, other):
#         return Circle(self.radius + other.radius)
    
# c1 = Circle(5)
# c2 = Circle(3)

# c3 = c1 + c2
# print(c3.radius)

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def add(self, other):
        return self.radius + other
    
c1 = Circle(5)
c2 = Circle(3)

print(c1.add(3))