n = int(input())
s = input().split()
sum = 0
for i in range(len(s)):
    for j in range(i):
        if int(s[i]) < int(s[j]):
            sum += 1
print(sum)
'''
n = int(input())
s = list(map(int,input().split()))
sum = 0
for i in range(len(s)):
    for j in range(i):
        if s[i] < s[j]:
            sum += 1
print(sum)
'''