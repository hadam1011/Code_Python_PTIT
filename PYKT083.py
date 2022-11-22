n = int(input())
data = {}
price = {
    "Xe_con5" : 10000,
    "Xe_con7" : 15000,
    "Xe_tai2" : 20000,
    "Xe_khach29" : 50000,
    "Xe_khach45" : 70000
}

for i in range(n):
    tokens = list(input().split())
    if tokens[3] == "OUT": continue
    if tokens[-1] not in data: data[tokens[-1]] = price[tokens[1] + tokens[2]]
    else: data[tokens[-1]] += price[tokens[1] + tokens[2]]

for i in data:
    print(i + ": " + str(data[i]))
