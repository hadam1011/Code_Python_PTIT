t = int(input())
while t > 0:
    s = input()
    a = list(s)
    a.sort(reverse=False)
    sum = 0
    for i in a:
        if i >= '0' and i <= '9':   sum += int(i)
        else:
            print(i,end='')
    print(sum)
    t -= 1
    