s = input()
k = int(input())
a = []
dem = []
ok = 0
for i in range(100): dem.append(0)
for i in range(0, len(s), 2):
    if i+1 < len(s):
        res = s[i] + s[i+1]
        dem[int(res)] += 1
        if res not in a: a.append(res)
a.sort()
for i in a:
    if dem[int(i)] >= k:
        ok = 1
        print(i, dem[int(i)])
if ok == 0:
    print("NOT FOUND")
