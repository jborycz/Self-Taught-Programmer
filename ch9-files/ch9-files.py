
### Ensures that path works for any operating system
import os
os.path.join("Users","bob","st.txt")

### How to open and close a file
st = open("st.txt","w")
st.write("Hi from Python!")
st.close()

### With statement allows automatic closing of files
with open("st.txt","w") as f:
    f.write("Hi from Python!")

### Reading from files with with statement
with open("st.txt","r") as f:
    print(f.read())

### Save file contents in list for later
my_list = list()

with open("st.txt","r") as f:
    my_list.append(f.read())

print(my_list)

### CSV (Comma Separated Values) - How to read and write
import csv

with open("st.csv","w",newline='') as f:
    w = csv.writer(f,delimiter=",")
    w.writerow(["one","two","three",])
    w.writerow(["four","five","six"])

with open("st.csv","r") as f:
    r = csv.reader(f,delimiter=",")
    for row in r:
        print(",".join(row))
