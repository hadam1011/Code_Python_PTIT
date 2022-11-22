def test_case ():
    n = input()
    for t in range(1000):
        if int(n) % 7 == 0:
            print(n)
            return
        n = str(int(n) + int(n[::-1]))
    print("-1")
t = int(input())
for i in range(t):
    test_case()
