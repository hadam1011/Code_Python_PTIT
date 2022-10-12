class sinhvien:
    def __init__(self,ma,ten,btl) -> None:
        self.ma = ma
        self.ten = ten
        self.btl = btl
    def getMa(self):
        return self.ma
    def getTen(self):
        return self.ten
    def getBtl(self):
        return self.btl
    
a = []
for t in range(int(input())):
    a.append(sinhvien(input(), input(), input()))

a.sort(key = lambda ele: [ele.getMa()])
for value in a:
    print(value.getMa(), value.getTen(), value.getBtl())