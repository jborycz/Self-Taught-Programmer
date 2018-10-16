import re

file=open('zen.txt','r')
file=file.read()
#print(file)

matches = re.findall('Dutch',file)

print(matches)
