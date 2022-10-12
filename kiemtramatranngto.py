import math 
def nto(n):
    if n < 2:
        return 0
    for i in range(2,int(math.sqrt(n)+1)):
        if n % i == 0:
            return 0
    return 1
n,m = map(int,input().split())
a = []
for i in range(n):
    a.append([int(j) for j in input().split()])
for i in range(n):
    for j in range(m):
        if nto(a[i][j]) == 1:
            print("1",end=" ")
        else:
            print("0",end=" ")
    print("")

        