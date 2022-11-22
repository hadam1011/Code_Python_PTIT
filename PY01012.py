s1 = input()
s2 = input()
p = int(input())
for i in range(0,p-1):
    print(s1[i], end='')
print(s2, end='')
for i in range(p-1,len(s1)):    
    print(s1[i],end='')
