import math
t = int(input())
while t > 0:
    n = int(input())
    print('1 * ', end='')
    for i in range(2 , int(math.sqrt(n) + 1)):
        dem = 0
        while n % i == 0:
            dem += 1
            n = int(n/i)
        if dem and n != 1: print(i, dem, sep='^', end=' * ')
        elif dem and n == 1: print(i, dem, sep='^', end='')
    if n > 1: print(n , 1, sep='^')
    else: print('')
    t-=1