chConst = '12345678910'

i = 11
pre = 1
while i < 1000001:
    if i % 10 == 0:
        pre += 1
    chConst += str(pre) + str(i % 10)
    i += 1
    
print int(chConst[0])*int(chConst[9])*int(chConst[99])*int(chConst[999])*int(chConst[9999])*int(chConst[99999])*int(chConst[999999])