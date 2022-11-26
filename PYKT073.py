n = int(input())
res = []
loai, dem = 0, 0

while n > 0:
    n -= 1
    l = len(input().split())
    if loai == 0: 
        loai = (2 if l == 7 else 1)
        res.append(loai)
    elif l == 7:
        dem += 1
        if dem == 4:
            loai = 2
            res.append(loai)    
            dem = 0
    elif loai == 2:
        loai = 1
        res.append(loai)

print(len(res))
for i in res: print(i)
