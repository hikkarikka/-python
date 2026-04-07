import math
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def length (self):
        return 2 * math.pi * self.radius

    def __eq__(self, value):
        return self.radius == value.radius
    
    def __gt__(self, value):
        return self.length() > value.length()
    
    def __lt__(self, value):
        return self.length() < value.length()
    
    def __ge__(self, value):
        return self.length() >= value.length()
    
    def __le__(self, value):
        return self.length() <= value.length()

    def __add__(self, value):
        return Circle(self.radius + value)
    
    def __sub__(self, value):
        return Circle(self.radius - value)
    
c1 = Circle(4)
c2 = Circle(6)
c3 = Circle(4)

print(c1 == c2)
print(c1 == c3)
print(c1 > c2)
print(c1 < c2)
print(c2 >= c3)
print(c3 <= c1)
c4 = c1 + 5
print(c4)
c5 = c2 - 2
print(c5)