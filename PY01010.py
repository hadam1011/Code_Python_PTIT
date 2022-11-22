t = int(input())
while t > 0:
    s = input()
    a = s[0] + s[1]
    b = s[len(s)-2] + s[len(s)-1]
    if a == b:
        print("YES")
    else:
        print("NO")
    t -= 1
    


