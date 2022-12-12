from decimal import Decimal, ROUND_HALF_UP

class HS:
    def __init__(self, ma, ten, diem):
        self.ma = f'HS{ma:02d}'
        self.ten = ten
        a = [Decimal(x) for x in diem.split()]
        tong = a[0] + a[1]
        for x in a:  tong += x

        self.tb = Decimal(tong) / Decimal(12)
        self.tb = self.tb.quantize(Decimal("0.1"), ROUND_HALF_UP)

        if self.tb >= 9: self.xl = "XUAT SAC"
        elif self.tb >= 8: self.xl = "GIOI"
        elif self.tb >= 7: self.xl = "KHA"
        elif self.tb >= 5: self.xl = "TB"
        else: self.xl = "YEU"
    
    def toString(self):
        return f'{self.ma} {self.ten} {self.tb} {self.xl}'

ls = []
for i in range(int(input())): ls.append(HS(i + 1, input(), input()))

ls.sort(key=lambda x : (-x.tb, x.ma))

for x in ls: print(x.toString())
