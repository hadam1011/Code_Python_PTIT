def thuannghich(n):
    s = str(n)
    s1=s[::-1]
    return s1 == s

def chan(n):
    s = str(n)
    for i in range(len(s)):
        a = int(s[i])
        if a % 2 == 1:
            return False
    return True
def check(n):
    s = str(n)
    if len(s) % 2 == 1:
        return False
    return True
t = int(input())
while t > 0:
    n = int(input())
    for i in range(22,n,22):
        if chan(i) == 1 and check(i) == 1 and thuannghich(i) == 1:
            print(i,end=" ")
    print("")
        
    t -= 1   
