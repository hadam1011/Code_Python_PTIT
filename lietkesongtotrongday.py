import math 
import collections
def nto(n):
    if n < 2:
        return 0
    for i in range(2,int(math.sqrt(n)+1)):
        if n % i == 0:
            return 0
    return 1

t = int(input())
a = list(map(int,input().split()))
b = dict.fromkeys(a)
for i in b:
    if nto(i) == 1:
        print(i,a.count(i))