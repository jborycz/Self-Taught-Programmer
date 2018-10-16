# 3
print("3")
def f(x,y,z,a=5,b=2):
    """
    Returns gt ls comparison
    :param a: int.
    :param b: int.
    :param x: int.
    :param y: int.
    :param z: int.
    :return: str and number comparison
    """
    a = input("a= ")
    b = input("b= ")
    a = int(a)
    b = int(b)
    c = a**3 + b**3
    w = x**2 + y**2 + z**2
    if c <= w:
        print(c,"<=",w)
        print("a^3 + b^3 <= x**2 + y**2 + z**2")
    else:
        print(w,"<=",c)
        print("x**2 + y**2 + z**2 <= a^3 + b^3")
f(3,3,3)
