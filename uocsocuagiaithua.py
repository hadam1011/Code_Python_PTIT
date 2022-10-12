import math
for i in range(int(input())):
    [n,p] = list(map(int,input().split()))
    res = 0
    x = 1
    while n/(p**x) > 1:
        res += int(n/(p**x))
        x += 1
    print(res)