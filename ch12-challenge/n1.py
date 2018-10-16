class Shape:
    def __init__(self,msg):
        self.msg = msg
    def what_am_i(self):
        return "I am a shape!"

class Rectangle(Shape):
    def __init__(self,l,w):
        self.length = l
        self.width = w
    def calculate_perimeter(self):
        return self.length*2 + self.width*2

class Square(Shape):
    def __init__(self,s,n):
        self.side = s
        self.new = n
    def calculate_perimeter(self):
        return self.side*4
    def change_size(self,new_side):
        self.side += new_side

class Horse():
    def __init__(self,b,c,rider):
        self.breed = b
        self.color = c
        self.rider = rider

class Rider():
    def __init__(self,name):
        self.name = name


#n1
rectangle = Rectangle(10,5)
print('n1=',rectangle.calculate_perimeter())
square = Square(6,0)
print('n1=',square.calculate_perimeter())

#n2
square.change_size(2)
print('n2=',square.calculate_perimeter())

#n3
print('n3=',square.what_am_i())
print('n3=',rectangle.what_am_i())

#n4
person = Rider("Zorro")
horse = Horse("Andalusian","black", person)
print(horse.rider.name)
