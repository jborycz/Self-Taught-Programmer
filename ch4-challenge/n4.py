# 4
print("4")
def func1(x):
    """
    Returns x/2
    :param x: int.
    :return: int div of x.
    """
    return x/2

def func2(y):
    """
    Returns y*4
    :param y: int.
    :return: int mult of y.
    """
    return y * 4

a = input("Type number: ")
a = int(a)
b = func1(a)
c = func2(b)
c = int(c)
print(c)
