import math
n = int(input())
a = []
for i in range(n):
    a.append([int(j) for j in input().split()])
dem1 = 0
dem2 = 0
for i in range(n):
    for j in range(n):
        if i + j < n-1:
            dem1 += a[i][j]
        elif i + j >= n:
            dem2 += a[i][j]
t = int(input())
x = math.fabs(dem1 - dem2)
if x <= t:
    print("YES")
else:
    print("NO")
print(int(x))

        