youin= [1,6,9,56,73,89,65,42,49,99,96,87,26,75]
x=0
while x != "q":
    x = input("Guess a number from 1 to 100 or type q to quit: ")
    try:
        x = int(x)
    except ValueError:
        x = str(x)
    if x in youin:
        print("You got it!")
        break
