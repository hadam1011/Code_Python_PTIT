a = []
while 1 :
    s = input().split(' ')
    a.extend(s)
    if len(a) == 10 : break
for i in range(len(a)):
    a[i] = int(a[i])%42
res = set(a)
print(len(res))
