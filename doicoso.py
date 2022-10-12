str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
str = list(str)

t = int(input())
for _ in range(t):
    s = input().split()
    a, b = int(s[0]), int(s[1])
    arr = []
    while a > 0:
        k = a % b
        if k < 10:  arr.append(k)
        else:
            for i in str:
                if k == ord(i) - 55:
                    arr.append(i)
                    break
        a = int(a/b)
    arr.reverse()
    for i in arr:
        print(i, end='')
    print('')