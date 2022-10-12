import math

dem = 0
s = input("").split()
a = int(s[0])
b = int(s[1])
for i in range(pow(10,b-1),pow(10,b)):
    if math.gcd(i,a) == 1:
        dem += 1
        print(i,end=" ")
        if dem % 10 == 0:
            print("")
    