def thuannghich(n):
    if n < 10:
        return 0
    s = str(n)
    s1=s[::-1]
    return s1 == s

def check(s):
    sum = 0
    for i in range(len(s)):
        a = int(s[i])
        sum += a
    return thuannghich(sum)


t = int(input())
while t > 0:
    s = input()
    if check(s) == 1:
        print("YES")
    else:
        print("NO")
    t -= 1
