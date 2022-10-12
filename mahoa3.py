char = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
char = list(char)
def xoay(a):
    giaTriXoay = 0
    for i in range(len(a)):
        giaTriXoay += char.index(a[i])
    for i in range(len(a)):
        id = ( char.index(a[i]) + giaTriXoay ) % 26
        a[i] = char[id]
    return a


_t = int(input())
for _ in range(_t):
    s = input()
    a = list( s[0:int(len(s)/2)] )
    b = list( s[int(len(s)/2):len(s)] )
    a = xoay(a)
    b = xoay(b)
    for i in range(len(a)):
        id = ( char.index(a[i]) + char.index(b[i]) ) % 26
        a[i] = char[id]
    for i in a: print(i, end='')
    print('')
