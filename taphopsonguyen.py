s = input().split()
a = set(list(map(int, input().split())))
b = set(list(map(int, input().split())))
print(*sorted(list(a & b)))
print(*sorted(list(a - b)))
print(*sorted(list(b - a)))
#cach chay
'''
s = input().split()
n, m = int(s[0]), int(s[1])
a = list(map(int, input().strip().split()))[:n]
b = list(map(int, input().strip().split()))[:m]
a.sort(reverse=False)
b.sort(reverse=False)
res1, res2, res3 = [], [], []
setA, setB = [], []
for i in a:
    if i not in setA: setA.append(i)
for i in b:
    if i not in setB: setB.append(i)
for i in setA:
    if i in setB: res1.append(i)
    else: res2.append(i)
for i in setB:
    if i not in setA: res3.append(i)
for i in res1:
    print(i, end=' ')
print('')
for i in res2:
    print(i, end=' ')
print('')
for i in res3:
    print(i, end=' ')
'''







