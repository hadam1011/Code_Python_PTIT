n,m = map(int,input().split())
a = list(map(int, input().split()))[:n]

dem = []
for i in range(0,m+1): dem.append(0)
for i in a: dem[i] += 1

ans = dem.copy()
dem.sort(reverse=True)
res = dem[0]
check = 0
for i in range(len(dem)):
    if res > dem[i]:
        res = dem[i]
        check = 1
        break
if check == 0 or res == 0: print("NONE")
else:
    for i in range(len(ans)):
        if ans[i] == res:
            print(i)
