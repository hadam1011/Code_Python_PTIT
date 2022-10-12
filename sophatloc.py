t = int(input())
while t > 0:
    s = input()
    s1 = s[len(s)-2] + s[len(s)-1]
    if s1 == "86":
        print("YES")
    else:
        print("NO")
    t -= 1