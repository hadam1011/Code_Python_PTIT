test = int(input())

for i in range(test):
    s1 = list(input())
    s2 = list(input())

    s1.sort()
    s2.sort()

    print(f"Test {i + 1}: YES" if s1 == s2 else f"Test {i + 1}: NO")
