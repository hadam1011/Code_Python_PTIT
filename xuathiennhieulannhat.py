
def check (a, n):
    mark = dict()
    cou_max = 0
    val_min = max(a)
    for i in a:
        if i in mark:
            mark[i] += 1
        else:   mark[i] = 1
        if (cou_max < mark[i]):
                cou_max = mark[i]
                val_min = i
        elif cou_max == mark[i] and val_min > i:
                val_min = i
    print(val_min if cou_max > n/2 else "NO")
for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    check(a, n)

    '''
t = int(input())
while t > 0:
    n = int(input())
    a = list(map(int, input().split()))
    x = max(set(a), key=a.count)
    if a.count(x) <= n/2:
        print("NO")
    else:
        print(x)
    t -= 1
    
    '''