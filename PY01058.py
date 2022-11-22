def nto(n):
    if n < 2:
        return 0
    for i in range(2,n):
        if n % i == 0:
            return 0
    return 1  

def check(s):
    s1 = s[len(s)-4] + s[len(s)-3] + s[len(s)-2] + s[len(s)-1] 
    return nto(int(s1))

t = int(input())
while t > 0:
    n = input()
    if check(n) == 1:
       print("YES")
    else:
        print("NO") 
    t -= 1   
