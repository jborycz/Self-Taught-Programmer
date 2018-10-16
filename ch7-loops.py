name = "Maleficent"
for character in name:
    print(character)

animals = ["dog", 
           "cat", 
           "turtle",
           "fish", 
           "horse", 
           "pig", 
           "sloth"]

for animal in animals:
    print(animal)

book = ["Tale of Two Cities","Catcher in the Rye","Moby Dick","The Devils"]
i=0
for story in book:
    new = book[i]
    new = new.lower()
    book[i] = new
    i+=1
    
print(book)


### Enumerate function
for i, story in enumerate(book):
    new = book[i]
    new = new.upper()
    book[i] = new

print(book)

for i in range(1,15):
    print(i)

### While loop
x=10
while x > 0:
#    print('{}'.format(x))
    print(x)
    x-=1
print("Happy New Year!")

### Break statement ends loop
x = 2
for i in range(0,20):
    if x<=100000:
        print(x)
        x=x*2
    else:
        print("TOO BIG!")
        break

### Nested loops
nums1=[2,4,6,8]
nums2=[8,6,4,2]
mult=[]
for i in nums1:
    for j in nums2:
        mult.append(i*j)
print(mult)
