test = int(input())
for i in range(test):
    a = input().split()
    if a[0] > a[1]:
        a[0], a[1] = a[1], a[0]
    
    try:
        x1 = input()
        x2 = input()
        x1 = x1.replace(a[1], a[0])
        x2 = x2.replace(a[1], a[0])
        print(int(x1) + int(x2), end=' ')

        x1 = x1.replace(a[0], a[1])
        x2 = x2.replace(a[0], a[1])
        print(int(x1) + int(x2))
    except:
        d = input().split(" ")
        print(int(d[0]) + int(d[1]), end=' ')
        
        d[0] = d[0].replace(a[0], a[1])
        d[1] = d[1].replace(a[0], a[1])
        print(int(d[0]) + int(d[1]))