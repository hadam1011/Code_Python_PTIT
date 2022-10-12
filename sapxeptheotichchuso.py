import math
def mul(n):
    tich = 1
    while n > 0:
        tich *= n%10
        n = int(n/10)
    return tich

t = int(input())
while t>0:
    n = int(input())
    a = list(map(int,input().split()))
    a.sort()
    b = sorted(a,key=mul)
    print(*b,sep=" ")
    t -= 1