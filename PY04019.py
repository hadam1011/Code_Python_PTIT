from decimal import Decimal, ROUND_HALF_UP

class TS:
    def __init__(self, ma, ten, lt, th):
        self.ma = f'TS0{ma}'
        self.ten = ten
        if lt > 10: lt /= 10
        if th > 10: th /= 10

        self.tb = Decimal(lt + th) / Decimal(2)
        self.tb = self.tb.quantize(Decimal("0.02"), ROUND_HALF_UP)

        if self.tb > 9.5: self.xl = "XUAT SAC"
        elif self.tb >= 8: self.xl = "DAT"
        elif self.tb >= 5: self.xl = "CAN NHAC"
        else: self.xl = "TRUOT"

    def toString(self):
        return f'{self.ma} {self.ten} {self.tb} {self.xl}'
    
ls = []
for i in range(int(input())):
    ls.append(TS(i + 1, input(), float(input()), float(input())))

ls.sort(key=lambda x: -x.tb)

for x in ls: print(x.toString())
