t = int(input())
while t > 0:
    n = input()
    a = list(n)
    for i in range(0,len(a)):   a[i] = int(a[i])
    for i in range(len(a)-1 , 0 , -1):
        if a[i] >= 5:
            a[i] = 0
            a[i-1] += 1
        else:
            a[i] = 0
    for i in range(0,len(a)):   print(a[i], end='')
    print('')
    t-=1