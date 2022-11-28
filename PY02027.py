import re
res = []
for i in range(int(input())):
    s=  input()
    m = re.findall(r'\d+', s)
    for j in m:
        res.append(int(j))  
res.sort()
for i in res:
    print(i)
