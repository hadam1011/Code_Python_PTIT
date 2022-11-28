def count(a, n):
    res = 0
    for x in a: res += abs(x - n)
    return res

n = int(input())
a = list(map(int, input().split()))

res = a[0]
steps = count(a, res)
for i in a:
    if count(a  , i) < steps:
        res = i
        steps = count(a, i)

print(f'{steps} {res}')
