def nto(n):
    if n < 2:
        return 0
    for i in range(2,n):
        if n % i == 0:
            return 0
    return 1  
t = int(input())
while t > 0:
    s = input()
    s1 = s[len(s)-4] + s[len(s)-3] +    s[len(s)-2] + s[len(s)-1]
    n = int(s1)
    if nto(n) == 1:
        print("YES")
    else:
        print("NO")
    t -= 1