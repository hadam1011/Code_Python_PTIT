from itertools import count


t = int(input())
while t>0:
    n = int(input())
    a = list(map(int, input().split()))
    dem =[]
    max1 = -1
    for i in a:
        if i > max1:
            max1 = i
    for i in range(max1+1):    dem.append(0)
    for i in a: dem[i] += 1
    for i in a:
        if dem[i] % 2 != 0:
            print(i)
            break
    t -= 1
