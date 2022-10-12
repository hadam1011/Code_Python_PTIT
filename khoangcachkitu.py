def reversed_string(text):
    result = ""
    for char in text:
        result = char + result
    return result
def check(s1,s2):
    for i in range(1, len(s1)):
        a = ord(s1[i]) - ord(s1[i-1])
        b = ord(s2[i]) - ord(s2[i-1])
        if abs(a) != abs(b):
            return False
    return True 

t = int(input())
while  t > 0:
    s1 = input("")
    s2 = reversed_string(s1)
    if check(s1,s2) == 1:
        print("YES")
    else:
        print("NO")
    t -= 1