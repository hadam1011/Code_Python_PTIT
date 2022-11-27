n = int(input())
a = [float(x) for x in input().split()]

check = [max(a), min(a)]

res = [x for x in a if x not in check]

cnt = float(0)
for x in res: cnt += x

print("%.2f" % (cnt / len(res)))
