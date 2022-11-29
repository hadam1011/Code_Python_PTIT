class CaThi:
    def __init__(self, ma, ngay, gio, phong):
        self.ma = f'C{ma:03d}'
        self.ngay = ngay
        self.gio = gio
        self.phong = phong
    
    def toSring(self):
        return f'{self.ma} {self.ngay} {self.gio} {self.phong}'

with open("CATHI.in") as file:
    ip = [s.strip() for s in file.readlines()]

ls, idx = [], 1
for i in range(int(ip[0])):
    ls.append(CaThi(i + 1 ,ip[idx], ip[idx + 1], ip[idx + 2]))
    idx += 3

ls.sort(key = lambda x: (x.ngay, x.gio, x.ma))

for x in ls: print(x.toSring())
