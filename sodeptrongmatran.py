n,m = map(int, input().split())
a = []
for i in range(n):
    hang = list(map(int, input().split()))
    a.append(hang)
res = []
ok, maxx, minn = 0, 0, 10000
for i in range(n):
    for j in range(m):
        if a[i][j] > maxx: maxx = a[i][j]
        if a[i][j] < minn: minn = a[i][j]
res = maxx - minn
k = 1
for i in range(n):
    for j in range(m):
        if a[i][j] == res:
            if k > 0:
                print(res)
                k -= 1
            ok = 1
            print('Vi tri [',i,'][' ,j, ']', sep='')
if ok == 0: print("NOT FOUND")