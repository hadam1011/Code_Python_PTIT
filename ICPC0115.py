import math 
def check(n):
    s = str(n)
    sum = 0
    for i in range(len(s)):
        sum += math.factorial(int(s[i]))
    return sum == n


t = int(input())
while t > 0:
    n = int(input())
    if check(n) == 1:
        print("Yes")
    else:
        print("No")
    t -= 1
