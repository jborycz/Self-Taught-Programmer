author = "dostoevsky"
print(author[0],author[1],author[2],author[3],author[4],author[5],author[6],author[7],author[8],author[9],author[-2],author[-3],author[-4],author[-5],author[-6],author[-7],author[-8],author[-9],author[0])

print("cat"+" in"+" hat")
print("Three"*3)

print("This will be capitalized".upper())
print("THIS WILL BE UNCAPITALIZED".lower())
print("first letter caps".capitalize())

### Format replaces {} with string
### Useful for user input
print("""The {} quick brown fox jumped {}.""".format("fucking","BITCH"))

### Split string into list with specified delimiter
print("1.2.3.4.5.6.7.8.9.10.11.12.13.14.15.16.17.18.19.20".split("."))

### Join allows adding of deliminter or combining list into single string
nums="123456789"
result="-".join(nums)
print(result)

testlist=["What","the","hell","!"]
onestring="".join(testlist)
splitonestring=" ".join(testlist)
print(onestring)
print(splitonestring)

### split lets you remove whitespace
test = "   White space     "
print(test)
print(test.strip())

### Replace every instance of one string with another
testreplace = "I am having a good time. Life is good. You are beautiful. I love you."
testreplace = testreplace.replace("good","shitty")
testreplace = testreplace.replace("beautiful","nasty")
testreplace = testreplace.replace("love","loath")
print(testreplace)

### Find first occurance of a string
x = "The turtledoves were shot by the monkey's aunt.".index("o")
print(x)

### Check if string in other string
print("Cat" in "Cat in hat.")

### Preface quotes in quotes with backslashes to include as strings
x = "He said, \"What?\""
print(x)

### \n indicates a new line
print("line1\nline2\nline3")

### Slicing allows lists or strings to be separated
### Leave last box blank to go to last
### Leave first blank to start at 0
numbers = "0123456789"
print(numbers[0:5])
print(numbers[2:])
