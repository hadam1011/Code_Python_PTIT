for t in range(int(input())):
    [n,k] = [int(x) for x in (input().split())]
    dem = 0
    while(k%2 == 0): 
        k = k / 2
        dem += 1
    
    print(chr(dem+65))