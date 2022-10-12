n = int(input())
a = []
for i in range(n):
    hang = input()
    hang = list(hang)
    a.append(hang)
dem = 0
for i in range(n):
    dem1 = 0
    dem2 = 0
    for j in range(n):
        if a[i][j] == "C": dem1 += 1
        if a[j][i] == "C": dem2 += 1   
    dem += int(dem1 * (dem1 - 1) / 2)
    dem += int(dem2 * (dem2 - 1) / 2)
print(dem)