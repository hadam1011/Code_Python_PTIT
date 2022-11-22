test = int(input())
for i in range(test):
    s = input()
    res = ""
    idx = 0
    while idx < len(s):
        cnt = 1
        pos = idx + 1
        while pos < len(s):
            if s[idx] == s[pos]:
                cnt += 1
                pos += 1
            else:
                break
        res += str(cnt) + s[idx]
        idx = pos
    print(res)
