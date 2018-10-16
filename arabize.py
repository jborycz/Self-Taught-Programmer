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
    o = int(0)
    z4 = number
    print(num,"= ",z1,"+ ",z2,"+ ",z3,"+ ",z4)
arabize()
