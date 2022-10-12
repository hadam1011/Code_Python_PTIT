test = int(input())
while test > 0:
    s = input().split()
    dem = 0
    while float(s[0]) < float(s[2]):
        s[0] = float(s[0]) + float(s[0]) * (float(s[1])/100)
        dem += 1
    if float(s[0]) == float(s[2]):
        dem-= 1
    print(dem)
    test -= 1