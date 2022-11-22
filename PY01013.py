def nto(n):
    if n < 2:
        return 0
    for i in range(2,n):
        if n % i == 0:
            return 0
    return 1

def uscln(a, b):
    if b == 0:
        return a
    return uscln(b, a % b)

t = int(input())
while t > 0:
    q = input().split()
    c = int(q[0])
    d = int(q[1])
    x = uscln(c,d)
    s = str(x)
    dem = 0
    for i in range(len(s)):
        dem += int(s[i])
    if nto(dem) == 1:
        print("YES")
    else:  
        print("NO")
    t -= 1
