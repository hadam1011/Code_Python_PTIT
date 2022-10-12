import math
from re import I

def check(n):
    s = 0
    if n%2 == 0:
        while n%2 == 0:
            s = s + 2
            n/=2
    for i in range(3,int(math.sqrt(n)+1),2):
        while n%i == 0:
            s += i 
            n /= i 
    if n > 1:
        s += n 
    return s

t = int(input(""))
tong = 0
while t > 0:
    n = int(input())
    tong += check(n)
    t -= 1
print("%.0d"%tong)


