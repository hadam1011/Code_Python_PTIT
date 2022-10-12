import math
def snt(n):
    if n < 2: return 0
    for i in range(2 , int(math.sqrt(n) + 1)):
        if n % i == 0: return 0
    return 1

def sum1(a,n):
    tong = 0
    for i in range(n+1):
        tong += a[i]
    return tong

def sum2(a,n):
    tong = 0
    for i in range(n+1,len(a)):
        tong += a[i] 
    return tong

n = int(input())
a = list(map(int,input().split()))[:n]

setA, check = [], 0
for i in a:
    if i not in setA: setA.append(i)
for i in range(len(setA)):
    if snt(sum1(setA,i)) and snt(sum2(setA,i)):
        print(i)
        check = 1
        break
if check == 0: print('NOT FOUND')
