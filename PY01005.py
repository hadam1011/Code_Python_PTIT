n = input("")
sum = 0
for i in range(len(n)):
    if  n[i] == "4":
        sum += 1
    if  n[i] == "7":
        sum += 1
if sum == 4 or sum == 7:
    print("YES")
else:
    print("NO")
    
