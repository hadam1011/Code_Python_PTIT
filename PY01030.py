def nto(n):
    if n < 2:
        return 0
    for i in range(2,n):
        if n % i == 0:
            return 0
    return 1   

def uscln(a, b):
    if b == 0:
        return a
    return uscln(b, a % b)
    

dem = 0
s = input("").split()
a = int(s[0])
b = int(s[1])
for i in range(pow(10,b-1),pow(10,b)):
    if uscln(i,a) == 1:
        dem += 1
        print(i,end=" ")
        if dem % 10 == 0:
            print("")
    
 
