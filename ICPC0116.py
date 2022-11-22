
def check(s):
    return s[0]==s[len(s)-1]

t = int(input())
while t > 0:
    n = input()
    if check(n) == 1:
        print("YES")
    else:
        print("NO")
    t -= 1
