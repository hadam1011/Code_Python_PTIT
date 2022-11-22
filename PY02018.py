n , check = int(input()) , 0
a = list(map(int, input().split()))
a.sort()
if a[0] > 1: print(a[0]-1)
else:
    for i in range(0,len(a)-1):
        if a[i] + 1 != a[i+1]:
            print(a[i] + 1)
            check = 1
            break
    if not check: print(max(a) + 1)
