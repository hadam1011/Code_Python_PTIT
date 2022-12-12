class GV:
    def __init__(self, ma, ten, maxt, d1, d2):
        self.ma = f'GV{ma:02d}'
        self.ten = ten  
        self.tong = d1 * 2 + d2
        if maxt[1:] == "1": self.tong += 2
        elif maxt[1:] == "2": self.tong += 1.5
        elif maxt[1:] == "3": self.tong += 1

        if maxt[0:1] == "A": self.mon = "TOAN"
        elif maxt[0:1] == "B": self.mon = "LY"
        else: self.mon = "HOA"

        if self.tong >= 18: self.tt = "TRUNG TUYEN"
        else: self.tt = "LOAI"

    def toString(self):
        return f'{self.ma} {self.ten} {self.mon} {self.tong} {self.tt}'
    
ls = []
for i in range(int(input())):
    ls.append(GV(i + 1, input(), input(), float(input()), float(input())))

ls.sort(key=lambda x : -x.tong)

for x in ls: print(x.toString())
