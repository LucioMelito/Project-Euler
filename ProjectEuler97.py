i = 100
dig = 10**3
last10 = [2**i % dig]

i += 1
while True:
    if 2**i % dig != last10[0]:
        last10.append(2**i % 10000000000)
        i += 1
    else:
        break
        
# notice that the last n-digits repeat themselves after 4*5**(n-1) times

rep = 4*5**(10 - 1)

power = 7830457 
newPower = power % rep

print (28433*2**(newPower)) % 10000000000 + 1