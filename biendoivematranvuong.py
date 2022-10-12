n, m = map(int, input().split())
a = []
for i in range(n):
    hang = list(map(int, input().split()))
    a.append(hang)
if n > m:
    dem = n - m
    for i in range(0,n,2):
        for j in range(m):
            if dem > 0: a[i][j] = -1
            else: break
        dem -= 1
else:
    dem = m - n
    for i in range(1,m,2):
        for j in range(n):
            if dem > 0: a[j][i] = -1
            else: break
        dem -= 1

for i in range(n):
    enter = 0
    for j in range(m):
        if a[i][j] != -1:
            enter = 1
            print(a[i][j], end=' ')
    if enter == 1: print('')