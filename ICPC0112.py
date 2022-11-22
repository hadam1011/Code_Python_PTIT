import math 
def nto(n):
    if n < 2:
        return 0
    for i in range(2,int(math.sqrt(n)+1)):
        if n % i == 0:
            return 0
    return 1
t = int(input())
while t > 0:
    n = int(input())
    dem = 0
    for i in range(2,n-6):
        if nto(i) and (nto(i+2) or nto(i+4)) and nto(i+6):
            dem += 1
    print(dem)
    t -= 1
