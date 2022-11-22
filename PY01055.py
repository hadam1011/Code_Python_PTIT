def check(s):
    for i in range(0,len(s)-3,2):
        if s[i+2] != s[i]:
            return False
    return True
  

def check1(s):
    if len(s) % 2 == 0:
        return False
    return True

def check2(s):
    return s[0] != s[1]

t = int(input())
while t > 0:
    n = input()
    if  check(n) ==1 and check1(n) == 1 and check2(n) == 1:
        print("YES")
    else:
        print("NO")   
    t -= 1  
