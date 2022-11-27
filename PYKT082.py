dict = {
    3:2.5, 4:2.5,
    5:3, 6:3, 
    7:3.5, 8:3.5, 9:3.5,
    10:4, 11:4, 12:4,
    13:4.5, 14:4.5, 15:4.5,
    16:5, 17:5, 18:5, 19:5,
    20:5.5, 21:5.5, 22:5.5,
    23:6, 24:6, 25:6, 26:6,
    27:6.5, 28:6.5, 29:6.5,
    30:7, 31:7, 32:7, 
    33:7.5, 34:7.5, 
    35:8, 36:8, 
    37:8.5, 38:8.5,
    39:9, 40:9
}

test = int(input())

for i in range(test):
    a = list(input().split())
    sum = float(0)
    for j in range(4): sum += (dict[int(a[j])] if j < 2 else float(a[j]))

    res = sum / 4
    if res - int(res) < 0.25: res = int(res) + 0.0
    elif res - int(res) < 0.75 and res - int(res) >= 0.25: res = int(res) + 0.5
    else: res = int(res) + 1.0

    print(res)
