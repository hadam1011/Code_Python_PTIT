t = int(input())
while t > 0:
    s = input().split()
    a = int(s[0])
    b = int(s[1])
    ds = input().split() 
    print(" ".join(ds[b:len(ds)])," ".join(ds[0:b])) 
    t -= 1