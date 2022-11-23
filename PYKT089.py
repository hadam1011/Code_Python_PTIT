n = int(input())
a = []
while True:
    for x in input().split(): a.append(int(x))
    if len(a) == n: break

chan = [x for x in a if x % 2 == 0]
le = [x for x in a if x % 2 != 0]

chan.sort()
le.sort(reverse = True)

chan_id = le_id = 0
for x in a:
    if x % 2 == 0: 
        print(chan[chan_id], end = " ")
        chan_id += 1
    else: 
        print(le[le_id], end = " ")
        le_id += 1
