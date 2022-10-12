dem1 = 0
dem2 = 0
s = input()
for i in range(len(s)):
    if s[i].isupper():
        dem1 += 1
    if s[i].islower():
        dem2 += 1
if dem1 <= dem2:
    print(s.lower())
else:
    print(s.upper())
        