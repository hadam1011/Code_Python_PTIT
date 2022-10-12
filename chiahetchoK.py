import math

a = list(map(int, input().split()))
list = []
start = math.ceil(a[0] / a[1])
end = math.floor(a[2] / a[1]) + 1

for i in range(start, end):    
    res = a[1] * i - a[0]
    if res > 0:
         list.append(res)

if len(list) == 0:
    print(-1)
else:
    for x in list:
        print(str(x) + " ",end="")