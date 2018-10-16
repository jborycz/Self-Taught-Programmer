# Challenges - pg 44
# 1
print("1")
print("wait")
print\
("but")
print("why?")
# 2
print("2")
import random
x=random.randint(0,20)
print("x=",x)
if x<10:
    print("x<10")
elif x>=10:
    print("x>=10")
# 3
print("3")
y=random.randint(0,35)
print("y=",y)
if y<=10:
    print("y<=10")
elif y>10 and y<=25: 
    print("y>10 and y<=25")
else:
    print("y>=25")

# 4
print("4")
x=random.randint(0,20)
y=random.randint(0,20)
print("x=",x,"and","y=",y)
z=x//y
print("z=",z)
a=x-z*y
print("remainder=",a)

# 5
print("5")
x=random.randint(0,20)
y=random.randint(0,20)
print("x=",x,"and","y=",y)
z1=x//y
z2=x/y
print("int quotient=",z1)
print("quotient=",z2)

# 6
print("6")
age=random.randint(0,100)
print("age=",age)
if age<=12:
    print("preteen")
elif age>12 and age<20: 
    print("teenager")
elif age>=20 and age<40: 
    print("young adult")
elif age>=40 and age<65: 
    print("middle age")
else:
    print("old")
