def nto(n):
    if n < 2:
        return 0
    for i in range(2,n):
        if n % i == 0:
            return 0
    return 1  

def check(s):
    for i in range(len(s)):
        if nto(i) == 1:
            if nto(int(s[i])) == 0:
                return False
        else:
            if nto(int(s[i])) == 1:
                return False
    return True         

t = int(input())
while t > 0:
    n = input()
    if check(n) == 1:
       print("YES")
    else:
        print("NO") 
    t -= 1   
