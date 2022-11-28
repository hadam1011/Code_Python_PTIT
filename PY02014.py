def count(ls, key):
    pre = next = 0
    for i in range(len(ls)):
        if ls[i] > key:
            pre = ls[i - 1]
            next = ls[i]
            break
    return min(key - pre, next - key)

check, ls = [1] * 10001, []
check[0] = check[1] = 0
for i in range(2, 10000):
    if check[i] == 1:
        ls.append(i)
        for j in range(i + i, 10000, i):
            check[j] = 0

n = int(input())
a = list(map(int, input().split()))

res = 0
for x in a:
    if check[x] == 0:
        res = max(res, count(ls, x))

print(res)
