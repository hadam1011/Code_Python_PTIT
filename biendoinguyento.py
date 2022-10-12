import math
prime = []
def isprime():
    prime.append(0)
    prime.append(0)
    for i in range(2, 10001): prime.append(1)
    for i in range(2 , int(math.sqrt(10001) + 1)):
        if prime[i]:
            for j in range(i*i , 10001 , i):
                prime[j] = 0
isprime()

n = int(input())
a = list(map(int, input().split()))[:n]

res = []
truoc = []
for i in a:
    if prime[i] == 0:
        res.append(i)
        while prime[i] == 0:
            i -= 1
        truoc.append(i)

sau = []
for i in a:
    if prime[i] == 0:
        while prime[i] == 0:
            i += 1
        sau.append(i)

ans = 0
for i in range(len(truoc)):
    ans = max( ans , min( sau[i] - res[i] , res[i] - truoc[i]) )

print(ans)
