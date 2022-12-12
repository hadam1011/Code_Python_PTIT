class Phim:
    def __init__(self, ma, matl, ngay, ten, sotap):
        self.ma = f'P{ma:03d}'
        self.sotap = sotap
        self.ngay = ngay
        self.ten = ten
        self.tl = dict[matl]
        self.cmp = ""
        for x in ngay.split('/')[::-1]: self.cmp += x

    def toString(self):
        return f'{self.ma} {self.tl} {self.ngay} {self.ten} {self.sotap}'

ls = []
dict = {}
n, m = map(int, input().split())

for i in range(n): dict[f'TL{(i + 1):03d}'] = input()

for i in range(m): ls.append(Phim(i + 1, input(), input(), input(), int(input())))
ls.sort(key=lambda x: (x.cmp, x.ten, -x.sotap))

for i in ls: print(i.toString())
