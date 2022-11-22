s = input()
a = []
dem = []
for i in range(100): dem.append(0)
for i in range(0, len(s), 2):
    if i+1 < len(s):
        res = s[i] + s[i+1]
        dem[int(res)] += 1
        if res not in a: a.append(res)
for i in a:
    print(i, dem[int(i)])
