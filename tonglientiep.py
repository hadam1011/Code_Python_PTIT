t = int(input())
while t > 0:
    n = int(input())
    dem = 0
    i = 1
    while i * (i + 1) < n * 2 :
        a = ( n - i * (i + 1) / 2 ) / (i + 1)
        if a == int(a): dem += 1
        i += 1
    print(dem)
    t -= 1