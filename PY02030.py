import math

def check(n):
    if n < 2: return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0: return False
    return True

n = int(input())
a = list(map(int, input().split()))

b = []
sumright = 0
for i in a:
    if i not in b:
        sumright += i 
        b.append(i)

index = 0
sumleft = b[0]
sumright -= b[0]

for i in range(len(b)):
    if check(sumright) and check(sumleft):
        print(index)
        break
    index += 1
    if index == len(b): break
    sumleft += b[i + 1]
    sumright -= b[i + 1]

if index == len(b): print("NOT FOUND")
