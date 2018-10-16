import math
x = math.pow(2,3)
print(x)

import random 
for i in range(0,10):
     x = random.randint(0,100)
     print(x)

 
import statistics 
# mean
nums = [4,6,7,5,1,4,6,9,4,2]
x = statistics.mean(nums)
# median 
y = statistics.median(nums)
# mode
z = statistics.mode(nums)
print(x,y,z)   

import keyword
x = keyword.iskeyword("for")
y = keyword.iskeyword("football")
print(x,y)
