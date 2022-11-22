import math
def sum(s):
    s1 = 0
    s2 = 0
    n = len(s)/2
    n = math.floor(n)
    for i in range(n):
        s1 = s1*10 + int(s[i])
    for i in range(n , len(s)):
        s2 = s2*10 + int(s[i])
    return s1 + s2

s = input()
if len(s) == 1: print(0)
else:
    while len(s) > 1:
        print(sum(s))
        s = str(sum(s))
