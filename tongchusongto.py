def nto(n):
    if n < 2:
        return 0
    for i in range(2,n):
        if n % i == 0:
            return 0
    return 1  

def check(s):
    sum = 0
    for i in range(len(s)):
        a = int(s[i])
        sum += a
    return nto(sum)

t = int(input())
while t > 0:
    s = input()
    if check(s) == 1:
        print("YES")
    else:
        print("NO")
    t -= 1 