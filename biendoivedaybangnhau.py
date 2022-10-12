def buoc(a,n):
    s = 0
    for i in a:
        s += abs(i-n)
    return s

n = int(input())
a = list(map(int, input().split()))[:n]

res = a[0]
ans = buoc(a,a[0])
for i in a:
    if buoc(a,i) < ans:
        ans = buoc(a,i)
        res = i
print(ans,res)    
    
