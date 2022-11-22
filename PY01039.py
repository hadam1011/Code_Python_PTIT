def check(s):
    for i in range(len(s)-2):
        a = int(s[i])
        b = int(s[i+1])
        c = int(s[i+2])
        if  a != c:
            return False
        if a == b:
            return False
    return True

t = int(input())
while t > 0:
    s = input()
    if check(s) == 1:
        print("YES")
    else:
        print("NO")
    t -= 1
