def readFile(filename):
    ls = set()
    with open(filename, 'r') as file:
        for s in file.readlines():
            for x in s.lower().split(): ls.add(x)
    return list(ls)

ls1 = readFile("DATA1.in")
ls2 = readFile("DATA2.in")
ls1.sort()
ls2.sort()

print(" ".join(s for s in ls1 if s not in ls2))
print(" ".join(s for s in ls2 if s not in ls1))
