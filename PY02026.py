s = input().split()
a = set(list(map(int, input().split())))
b = set(list(map(int, input().split())))
if a==b:
    print("YES")
else:
    print("NO")
