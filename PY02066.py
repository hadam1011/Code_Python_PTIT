n = int(input())
ls = []
while True:
    for x in input().split(' '): ls.append(int(x))
    if len(ls) == n: break

if n == ls[-1]: print("Excellent!") 
else:
    count = 1
    while count < ls[-1]:
        if count not in ls: print(count)
        count += 1
