p = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_.'
while 1:
    n = input()
    arr = n.split(' ')
    k = int(arr[0]) 
    if k == 0: break
    s = arr[1]
    res = []
    for i in range(len(s)):
        index = p.index(s[i])
        res.insert(i,p[(index + k) % 28])
    res.reverse()
    for i in res:
        print(i,sep='',end='')
    print('')
