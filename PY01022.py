n = input()
sum = 0
def sumDigit(s):
    tong = 0
    for value in s:
        tong = tong + ord(value) - ord('0')
    return str(tong)

while True:
    if len(n) == 1:
        break
    n = sumDigit(n)
    sum += 1
print(sum)
