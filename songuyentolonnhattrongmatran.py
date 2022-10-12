import math
def check(n):
    if n < 2: return 0
    for i in range(2 , int(math.sqrt(n) + 1)):
        if n % i == 0: return 0
    return 1

n,m = map(int, input().split())
a = []
for i in range(n):
    hang = list(map(int, input().split()))
    a.append(hang)
res = []
ok = 0
for i in range(n):
    for j in range(m):
        if check(a[i][j]):
            ok = 1
            res.append(a[i][j])
if ok == 0: print("NOT FOUND")
else:
    maxx = max(res)
    print(maxx)
    for i in range(n):
        for j in range(m):
            if a[i][j] == maxx:
                print('Vi tri [',i,'][' ,j, ']', sep='')
