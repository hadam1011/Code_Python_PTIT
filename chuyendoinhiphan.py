dec_number= int('10010100010010101', 2)
a = []
while dec_number > 0:
    a.append(dec_number%8)
    dec_number = dec_number // 8
    
for i in a:
    print(i)
