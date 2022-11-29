def convert(n):
    ind, res = len(n) - 1, 0
    while ind >= 0:
        if(n[ind] == '1'): res += pow(2, len(n) - ind - 1)
        ind -= 1
    return res    

with open("DATA.in") as file:
    ip = [s.strip() for s in file.readlines()]

dict1 = {
    2 : 1,
    4 : 2,
    8 : 3,
    16 : 4
}

dict2 = {
    0 : '0', 1 : '1', 2 : '2', 3 : '3', 4 : '4', 5 : '5', 
    6 : '6', 7 : '7', 8 : '8', 9 : '9', 10 : 'A', 
    11 : 'B', 12 : 'C', 13 : 'D', 14 : 'E', 15 : 'F'
}

for i in range(1, len(ip) - 1, 2):
    b, s = int(ip[i]), ip[i + 1] 
    index, res = len(ip[i + 1]), []
    while index - dict1[b] >= 0:
        res.append(dict2[convert(ip[i + 1][index - dict1[b] : index])])
        index -= dict1[b]

    mod = len(ip[i + 1]) % dict1[b]
    if mod != 0: res.append(dict2[convert(ip[i + 1][:mod])])

    res.reverse()
    while res[0] == '0': 
        if len(res) == 1: break
        res.pop(0)

    for x in res: print(x, end='')
    print()

    
