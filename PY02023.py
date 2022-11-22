import math
def sum(n):
    tong = 0
    while n > 0:
        tong += n%10
        n = int(n/10)
    return tong

t = int(input())
while t>0:
    n = int(input())
    a = list(map(int,input().split()))
    a.sort()
    b = sorted(a,key=sum)
    print(*b,sep=" ")
    t -= 1
