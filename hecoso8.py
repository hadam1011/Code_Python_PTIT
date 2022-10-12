n = input()
x, mu = 0, 0
res = []
for i in range(len(n)-1 , -1, -1):
    x += int(n[i]) * pow(2,mu)
    mu += 1
    if mu == 3:
        res.append(x)
        x, mu = 0, 0
if x: res.append(x)

res.reverse()
for i in res:
    print(i, end='')