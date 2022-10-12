n = int(input())
a = list(map(float, input().split()))
maxx = max(a)
minn = min(a)
sum , dem = 0 , 0
for i in a:
    if i != minn and i != maxx:
        sum += i
        dem += 1
sum = sum/dem
print("%.2f"%sum)