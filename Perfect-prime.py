import math 
def nto(n):
    if n < 2:
        return 0
    for i in range(2,int(math.sqrt(n)+1)):
        if n % i == 0:
            return 0
    return 1

def check(n):
    s = str(n)
    s1 = s[::-1]
    return nto(int(s1))

def check1(n):
    s = str(n)
    sum = 0
    for i in range(len(s)):
        sum += int(s[i])
    return nto(sum)
def check2(n):
    s = str(n)
    for i in range(len(s)):
        if nto(int(s[i])) == 0:
            return False
    return True

t = int(input())
while t > 0:
    n = int(input())
    if nto(n) == 1 and check(n) == 1 and check1(n) == 1 and check2(n) == 1:
        print("Yes")
    else:
        print("No")
    t -= 1