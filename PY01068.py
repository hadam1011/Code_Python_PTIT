import itertools

n, k = list(map(int, input().split()))
a = set(list(input().split()))

res = []
for s in list(itertools.combinations(list(a), k)):
    str = list(s)
    str.sort()
    res.append(str)

res.sort()
for s in res: print(" ".join(s))
