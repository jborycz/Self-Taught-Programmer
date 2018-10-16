# 1
musicians = ["Elton John","Josh Homme","Iggy Pop","Les Claypool","Brahms","Eminem","Aesop Rock"]

#2
lived = []
knoxville = (35.960638,-83.920739)
minneapolis = (44.977753,-93.265011)
davison = (43.034749,-83.518006)
holland = (42.787523,-86.108930)
moline = (41.506700,-90.515134)
mora = (45.876903,-93.293835)
youngstown = (41.099780,-80.649519)
lived.append(knoxville)
lived.append(minneapolis)
lived.append(davison)
lived.append(holland)
lived.append(moline)
lived.append(youngstown)

#3 
attributes = {"height":"6ft 2in",
              "weight":"180 lbs",
              "eye color":"blue",
              "shoe size":"10",
              "name":"Joshua",
              "sex":"Male",
              "hair":"Brown"}

#4
n = input("What do you wanna know about me: ")
if n in attributes:
    query = attributes[n]
    print(query)
else:
    print("I can't tell you.")

#5
songs = ["Benny and the Jets","Fortress","Gardenia","John the Fisherman","Hungarian Dance #11","Rap God","Shrunk"]
pairedup = {musicians[0]:songs[0],
             musicians[1]:songs[1],
             musicians[2]:songs[2],
             musicians[3]:songs[3],
             musicians[4]:songs[4],
             musicians[5]:songs[5],
             musicians[6]:songs[6]}
print(pairedup)

#6 

### A Set is an unordered set of unique elements.
