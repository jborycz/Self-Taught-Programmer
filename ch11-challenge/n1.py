import math
#n1
class Apple:
    def __init__(self, c, t, a, p):
        self.color = c
        self.type = t
        self.age = a
        self.price = p

#n2
class Circle:
    def __init__(self, r):
        self.len = r

    def area(self):
        return self.len*self.len*math.pi

    def change(self, r):
        self.len = r

circle = Circle(10)
print('circle1=',circle.area())
circle.change(20)
print('circle2=',circle.area())

#n3
class Triangle:
    def __init__(self, b, h):
        self.base = b
        self.height = h

    def area(self):
        return 0.5*self.base*self.height

    def change(self, b, h):
        self.base = b
        self.height = h

triangle = Triangle(5, 10)
print('triangle1=',triangle.area())
triangle.change(6, 11)
print('triangle2=',triangle.area())

#n4
class Hexagon:
    def __init__(self, s):
        self.side = s

    def calculate_perimeter(self):
        return self.side*6

    def change(self, s):
        self.side = s

hexagon = Hexagon(5)
print('hexagon1=',hexagon.calculate_perimeter())
hexagon.change(7)
print('hexagon2=',hexagon.calculate_perimeter())

    
