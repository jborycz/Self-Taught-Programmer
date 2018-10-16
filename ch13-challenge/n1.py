class Square:
    square_list = []
    def __init__(self,side):
        self.side = side
        self.square_list.append(self.side)
    def __repr__(self):
        return """{} by {} by {} by {}""".format(self.side, self.side, self.side, self.side)
    def side_length(self):
        return self.side

square1 = Square(10)
square2 = Square(12)
square3 = Square(14)

#n1
print(Square.square_list)

#n2
print(square1)

#n3
class Gender:
    def __init__(self,mw):
        self.mw = mw
    def __repr__(self):
        return self.mw

Susan = Gender("woman")
Joe = Gender("man")
Steve = Joe
Carol = Susan

print(Susan is Carol)
print(Susan is Steve)
print(Carol is Steve)
print(Steve is Joe)
        
