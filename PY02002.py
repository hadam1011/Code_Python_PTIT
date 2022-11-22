def fibo(n):
    f0 = 0
    f1 = 1
    fn = 1
 
    if (n < 0):
        return -1
    elif (n == 0 or n == 1):
        return n
    else:
        for i in range(2, n):
            f0 = f1
            f1 = fn
            fn = f0 + f1
        return fn
 
t = int(input())
while t > 0:
    n = input().split()
    a = int(n[0])
    b = int(n[1])
    for i in range(a,b+1):
        print(fibo(i),end=" ")
    print("")
    t -= 1

