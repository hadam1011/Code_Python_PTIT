import math

def nto(n):
    if len(str(n)) < 2: return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0: return False
    return True

n, m = list(map(int, input().split()))
a = []
check, res = 0, 0

for i in range(n):
    a.append([int(x) for x in input().split()])
    for x in a[i]:
        if nto(x): res = max(res, x)

for i in range(n):
    for j in range(m):
        if a[i][j] == res:
            if check == 0: print(res) 
            print(f'Vi tri [{i}][{j}]')
            check = 1

if check == 0: print("NOT FOUND")
