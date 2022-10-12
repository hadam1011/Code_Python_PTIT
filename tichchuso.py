
def check(s):
    sum = 1
    for i in range(len(s)):
        a = int(s[i])
        if a != 0:
            sum = sum*a
    return sum 

t = int(input())
while t > 0:
    s = input()
    print(check(s))
           
    t -= 1