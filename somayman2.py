def check(n):
    n = input("")
    sum = 0
    for i in range(len(n)):
        if  n[i] != "4" and n[i] != "7":
           return False
    return True
        
       
t = int(input(""))
a = []
for i in range(t):
    a.append(i)
for i in range(t):
    if check(a[i] == 1):
        print("YES")
    else:
        print("NO")