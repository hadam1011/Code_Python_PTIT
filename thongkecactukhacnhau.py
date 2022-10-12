def check(x):
    if ( x >= 'a' and x <= 'z' ) or ( x >= 'A' and x <= 'Z' ) or( x >='0' and x <= '9') or x == ' ' :
        return 1
    return 0

n = int(input())
res = ''
for i in range(n):
    s = input()
    for j in s:
        if check(j): res += j
        else: res += ' '
    res += ' '
res = res.lower().split()
setS = []
for i in res:
    if i not in setS:   setS.append(i)
setS.sort()
setCount = []
for i in res:
    tmp = res.count(i)
    if tmp not in setCount: setCount.append(tmp)
setCount.sort(reverse=True)
for i in setCount:
    for j in setS:
        if res.count(j) == i:
            print(j, i)