### Methods
print("Hello".upper())
print("Hello".replace("o","@"))

### Lists
fruit = list()
veg = ["carrot","green bean","potato"]
print(veg)
veg.append("onion")
print(veg)
random = []
random.append(True)
random.append("butt")
random.append(1.987)
random.append(veg)
print(random)
print(random[2])
random[2] = 7.891
print(random)

# pop removes last item from list
item = veg.pop()
print(item)
print(veg)

# Combine lists
veg = veg + random
print(veg)

# in and not in can check if something is in list
if "carrot" in veg:
    print("Yep")
elif "carrot" not in veg:
    print("Nope")

# size of list
len(veg)

### Tuples - immutable lists
# my_tuple = tuple()
# my_tuple = ()
# tuple: ("tuple",) - must add comma!
# not a tuple: ("tuple")
rndm = ("legs","thighs",3.14159,False)
print(rndm)

### Dictionaries
# Link key to value via mapping
# Curly brackets
# my_dict = dict()
# my_dict = {}
fruits = {"Apple":"Red","Banana":"Yellow"}
print(fruits)
fruits["Sky"] = "Blue"
del fruits["Apple"]
print(fruits)

