def check(n):
    if n < 10: return 0
    m, k = 0, n
    while n > 0:
        m = m*10 + n%10
        n = int(n/10)
    if m == k: return 1
    return 0


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
