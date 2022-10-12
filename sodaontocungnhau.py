def nto(n):
    if n < 2:
        return 0
    for i in range(2,n):
        if n % i == 0:
            return 0
    return 1   

def uscln(a, b):
    if b == 0:
        return a
    return uscln(b, a % b)

t = int(input(""))
while t > 0:
    s1 = input()
    s2 = s1[::-1]
    a = int(s1)
    b = int(s2)
    if  uscln(a,b) == 1:
        print("YES")
    else:
        print("NO")
    t-=1