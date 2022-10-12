t = int(input())
while t > 0:
    s = input()
    i = 0
    while i < len(s):
        x = s[i]
        d = 0
        for j in range(i, len(s)):
            if(s[i]==s[j]):
                d += 1
            else:
                break
        i = i + d
        print(d,end='')
        print(x,end='')
    print("")
    t -= 1
