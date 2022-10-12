import math
def check(n):
    if n < 2:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

t = int(input())
while t > 0:
    s = input()
    a = int(s[0] + s[1] + s[2])
    b = int(s[len(s)-3] + s[len(s)-2] + s[len(s)-1])
    if check(a) == 1 and check(b) == 1:
        print("YES")
    else:
        print("NO")
    t -= 1
