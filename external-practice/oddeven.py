num = input("Input a number: ")
num = int(num)

check = num % 2
check4 = num % 4

if check4 == 0:
    print("Divisible by 4")
elif check == 0:
    print("even")
else:
    print("odd")
