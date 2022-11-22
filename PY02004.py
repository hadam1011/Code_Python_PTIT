n = int(input())
s = input().split()
sum = 0
for i in range(len(s)-1):
    if int(s[i]) + int(s[i + 1]) == 1:
        sum += 1
print(sum)
