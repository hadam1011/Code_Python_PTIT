import math 
def nto(n):
    if n < 2:
        return 0
    for i in range(2,int(math.sqrt(n)+1)):
        if n % i == 0:
            return 0
    return 1
s = input().split(' ')
n, x = int(s[0]), int(s[1])
print(x, end=' ')
res = x
i = 0
while n > 0:
    if nto(i):
        res += i
        print(res,end=' ')
        n-=1
    i+=1
