def solve(n):
    dem = 0
    if n[0] != '6': return 0
    for i in n:
        dem += 1
        if i != '6' and i != '8':   return 0
        if i == '6':    dem = 0
        if dem == 3 and i != '6':   return 0
    return 1

n = input()
if solve(n): print("YES")
else: print("NO")
