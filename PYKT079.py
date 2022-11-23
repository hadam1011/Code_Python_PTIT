t = int(input())
while t>0:
    n = int(input())
    a = list(map(int, input().split()))
    b = set(a)
    x = max(b)
    y = min(b)
    print(x-y+1-len(b))
    t -= 1
