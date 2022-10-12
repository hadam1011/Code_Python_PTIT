
def check(s):
    sum = 0
    for i in range(len(s)):
        a = int(s[i])
        sum += a
    return sum % 3 == 0

t = int(input())
while t > 0:
    s = input()
    if check(s) == 1:
        print("YES")
    else:
        print("NO")
    t -= 1