def check(a,b,n):
    for i in range(n):
        if a[i] > b[i]:
            return False
    return True
t = int(input())
while t > 0:
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort()
    if check(a,b,n)==1:
        print("YES")
    else:
        print("NO")
    t -= 1
    
