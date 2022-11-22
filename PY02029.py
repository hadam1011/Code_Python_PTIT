def key(n):
  return dict[n]

n, m = list(map(int, input().split()))
a = list(map(int, input().split()))

dict = {}
for i in a:
  if i in dict: dict[i] += 1
  else: dict[i] = 1

res = [x for x in dict if dict[x] < max(list(dict.values()))]

res.sort(key = key)

if len(res) == 0: print("NONE")
else: print(res[-1])
