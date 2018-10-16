def f(x):
    """
    Returns floating pt of x
    :param x: str.
    :return: float of x. 
    """
    try:
        return float(x)
    except ValueError:
        print("That was not a number!")

x = input("Write any number: ")
print(f(x))
