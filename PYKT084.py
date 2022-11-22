n = int(input())
dict = {}
is_topic = True
topic = ""
for i in range(n):
    s = input()
    if is_topic:
        topic = s
        dict[topic] = 0
        is_topic = False
        continue

    if len(s) == 0:
        is_topic = True 
        continue
    dict[topic] += 1

for x in dict: print(f'{x}: {dict[x]}')

    

