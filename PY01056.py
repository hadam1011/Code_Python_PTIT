def nto(n):
    if n < 2:
        return 0
    for i in range(2,n):
        if n % i == 0:
            return 0
    return 1  

def check(s):
    for i in range(0,len(s),2):
        if int(s[i]) % 2 == 1:
            return False 
    return True

def check1(s):
    for i in range(1,len(s)-1,2):
        if int(s[i]) % 2 == 0:
            return False 
    return True

def check2(s):
    sum = 0
    for i in range(0,len(s)):
        sum += int(s[i])
    return nto(sum)

t = int(input())
while t > 0:
    n = input()
    if check(n) == 1 and check1(n) == 1 and check2(n) == 1:
       print("YES")
    else:
        print("NO") 
    t -= 1   
