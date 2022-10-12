t = int(input())
while t > 0:
    n = int(input())
    a = []
    for j in range(n):
        x = int(input())
        a.append(x)
    a.sort()
    maxx, res = a.count(a[0]), a[0]
    for i in range(len(a)):
        if a.count(a[i]) > maxx:
            maxx = a.count(a[i])
            res = a[i]
    print(res)
    t -= 1