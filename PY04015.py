class HD:
    def __init__(self, ma, ten, cu, moi):
        self.ma = f'KH{ma:02d}'
        self.ten = ten

        dis = moi - cu
        if dis > 100:
            self.tong = 50 * 100
            self.tong += 50 * 150
            self.tong += (dis - 100) * 200
            self.tong += self.tong * 0.05
        elif dis > 50:
            self.tong = 50 * 100
            self.tong += (dis - 50) * 150
            self.tong += self.tong * 0.03
        else:
            self.tong = dis * 100
            self.tong += self.tong * 0.02
    
    def toString(self):
        return f'{self.ma} {self.ten} {round(self.tong)}'

ls = []
for i in range(int(input())):
    ls.append(HD(i + 1, input(), int(input()), int(input())))

ls.sort(key=lambda x: -x.tong)

for x in ls: print(x.toString())
