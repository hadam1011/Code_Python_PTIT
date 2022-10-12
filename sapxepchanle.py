n = int(input())
arr = []
ok = 0
while(1):
    s = input().split()
    for i in s:
        arr.append(int(i))
        if len(arr) == n:
            ok = 1
            break
    if ok: break

chan, le, c, l = [], [], 0, 0
for i in arr:
    if i % 2 == 0: chan.append(i)
    else: le.append(i)
chan.sort(reverse=False)
le.sort(reverse=True)
for i in arr:
    if i % 2 == 0:
        print(chan[c], end=' ')
        c += 1
    else:
        print(le[l], end=' ')
        l += 1
