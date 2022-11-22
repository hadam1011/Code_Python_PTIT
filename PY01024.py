def check1(n):
    for i in range(len(n)-1):
        if abs(int(n[i]) - int(n[i+1])) != 2:
            return False
    return True

def check(n):
    sum = 0
    for i in range(len(n)):
        sum += int(n[i])
    return sum % 10 == 0

t = int(input())
while t > 0:
    s = input()
    if check1(s) == 1 and check(s) == 1:
        print("YES")
    else:
        print("NO")
    t -= 1


