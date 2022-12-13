class LT:
    def __init__(self, ma, mamon, ngay, gio, nhom):
        self.ma = f'T{ma:03d}'
        self.mamon = mamon
        self.ngay = ngay
        self.gio = gio
        self.nhom = nhom
        self.ten = dict[self.mamon]

        self.cmpNgay = ""
        for x in ngay.split('/')[::-1]: self.cmpNgay += x

    def to_string(self):
        return f'{self.ma} {self.mamon} {self.ten} {self.ngay} {self.gio} {self.nhom}'

dict = {}
ls = []
n, m = map(int, input().split())
for i in range(n):
    ma = input()
    dict[ma] = input()

for i in range(m):
    a = input().split()
    ls.append(LT(i + 1, a[0], a[1], a[2], a[3]))

ls.sort(key=lambda x: (x.cmpNgay, x.gio, x.ma))

for x in ls: print(x.to_string())
