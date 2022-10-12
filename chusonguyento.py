def nto(n):
    if n < 2:
        return 0
    for i in range(2,n):
        if n % i == 0:
            return 0
    return 1  

def check(s):
    if nto(len(s)) == 0:
        return False
    return True

def check1(s):
    dem1,dem2 = 0,0
    for i in range(len(s)):
        a = int(s[i])
        if nto(a) == 1:
            dem1 += 1
        else:
            dem2 += 1
    return dem1 > dem2

t = int(input())
while t > 0:
    s = input()
    if check(s) == 1 and check1(s) == 1:
        print("YES")
    else:
        print("NO")
    t -= 1