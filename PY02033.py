# s = input()
# a = []
# for i in range(0, len(s), 2):
#     if i+1 < len(s):
#         res = s[i] + s[i+1]
#         if res not in a: a.append(res)
# for i in a:
#     print(i, end=' ')


s = input()
a = []
for i in range(1,len(s),2):
    x = int(s[i-1:i+1])
    if x not in a: a.append(x)

for i in a:
     print(i, end=' ')
