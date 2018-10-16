# Function
# Never use caps! Use underscores!
def f(x):
    return x * 2
x=4
result = f(6)
print(f(x))
print(result)

def f():
    return 6 * 6
result = f()
print(result)

def f(x,y,z):
    return x**2 + y**2 +z**2
result = f(2,3,4)
print(result)

# len prints number of characters
z = len("shit on a shingle")
print(z)
# str converts to string
# int converts to integer
# float converts to floating pt number
z = str(390480.0918234)
y = int("123")
print(z, y)

## input command asks for input in shell
#yob = input("Enter your year of birth: ")
#z = int(yob)
#x = 2018 - z
#y = int(x)
#print("You are",y,"years old!")

# Reusability of functions required params
def arabize():
    num = input("Enter a number less than 10,000: ")
    number = int(num)
# Thousands place
    th = number//1000
    th1 = int(th)
    z1 = th1 * int(1000)
    number = number - z1
# Hundreds Place
    h = number//100
    h1 = int(h)
    z2 = h1 * int(100)
    number = number - z2
# Tens place
    t = number//10
    t1 = int(t)
    z3 = t1 * int(10)
    number = number - z3
# Ones place
    z4 = number
    print(num,"= ",z1,"+ ",z2,"+ ",z3,"+ ",z4)
arabize()

# Function with optional parameters
def f(x=2):
    return x**x
print(f())
print(f(6))

## Write to global variable
#global x
#x+=1

# Exception handling
try:
    a=input("type a number: ")
    b=input("type another: ")
    a=int(a)
    b=int(b)
    print(a/b)
except(ZeroDivisionError,ValueError):
    print("Either you divided by zero or that ain't a number!")
