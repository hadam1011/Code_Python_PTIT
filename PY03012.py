class sinhvien:
    def __init__(self,ten,hw,sub) -> None:
        self.ten = ten
        self.hw = hw
        self.sub = sub

    def getTen(self):
        return self.ten
    def getHw(self):
        return self.hw
    def getSub(self):  
        return self.sub 
def check(self):
    for i in a:
        if sel

a = []
for t in range(int(input())):
    ten = input()
    hw, sub = list(map(int,input()))
    a.append(sinhvien(ten, hw, sub))

a.sort(key = check)
for value in a:
    print(value.getMa(), value.getTen(), value.getBtl())
