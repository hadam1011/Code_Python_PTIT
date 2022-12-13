class TS:
    def __init__(self, ma, ten, diem, dt, kv):
        self.ma = f'TS{ma:02d}'
        self.ten = " ".join(ten.lower().strip().title().split())
        
        if kv == 1: self.tong = diem + 1.5
        elif kv == 2: self.tong = diem + 1
        else: self.tong = diem

        if dt != "Kinh": self.tong += 1.5

        self.tt = ("Do" if self.tong >= 20.5 else "Truot")
    
    def toString(self):
        return f'{self.ma} {self.ten} {self.tong} {self.tt}'

ls = []
for i in range(int(input())):
    ls.append(TS(i + 1, input(), float(input()), input(), int(input())))

ls.sort(key=lambda x: (-x.tong, x.ma))

for x in ls: print(x.toString())
