import math

def Check(n):
    if n == 1:
        return 0
    for i  in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return 0
    return 1

test = int(input())
for i in range(test):
    n = input()
    last = int(n[-3 : len(n)])
    head = int(n[: 3])
    if Check(last) == 1 and Check(head) == 1:
        print("YES")
    else:
        print("NO")
