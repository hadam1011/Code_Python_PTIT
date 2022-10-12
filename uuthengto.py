def nto(n):
    if n < 2:
        return 0
    for i in range(2,n):
        if n % i == 0:
            return 0
    return 1  

def check(s):
    return nto(len(s))

def check1(s):
    dem = 0
    dem1 = 0
    for i in range(len(s)):
        if nto(int(s[i])) == 1:
            dem1 += 1
        else:
            dem += 1 
    return dem1 > dem

t = int(input())
while t > 0:
    n = input()
    if check(n) == 1 and check1(n) == 1:
       print("YES")
    else:
        print("NO") 
    t -= 1   