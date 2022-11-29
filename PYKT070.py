listCa = []
listMon = []

class MonThi:
    def __init__(self, ma, ten, thi):
        self.ma = ma
        self.ten = ten
        self.thi = thi

class CaThi:
    def __init__(self, ma, ngay, gio, phong):
        self.ma = f'C{ma:03d}'
        self.ngay = ngay
        self.gio = gio
        self.phong = phong

class LichThi:
    def __init__(self, s):
        ip = [str for str in str(s).split()]
        for x in listCa:
            if x.ma == ip[0]:
                self.ngay = x.ngay
                self.gio = x.gio
                self.phong = x.phong
                break
        
        for x in listMon:
            if x.ma == ip[1]:
                self.ten = x.ten
                break
        self.ma_ca = ip[0]
        self.nhom = ip[2]
        self.sl = ip[3]

    def toString(self):
        return f'{self.ngay} {self.gio} {self.phong} {self.ten} {self.nhom} {self.sl}'

def nhapMT():
    with open("MONTHI.in") as file:
        mt = [s.strip() for s in file.readlines()]

    idx = 1
    for i in range(int(mt[0])):
        listMon.append(MonThi(mt[idx], mt[idx + 1], mt[idx + 2]))
        idx += 3
    
def NhapCT():
    with open("CATHI.in") as file:
        ct = [s.strip() for s in file.readlines()]
    
    idx = 1
    for i in range(int(ct[0])):
        listCa.append(CaThi(i + 1, ct[idx], ct[idx + 1], ct[idx + 2]))
        idx += 3

listLich = []
NhapCT()
nhapMT()
with open("LICHTHI.in") as file:
    lt = [s.strip() for s in file.readlines()]

for i in range(int(lt[0])):
    listLich.append(LichThi(lt[i + 1]))

listLich.sort(key = lambda x: (x.ngay, x.gio, x.ma_ca))

for x in listLich: print(x.toString())
