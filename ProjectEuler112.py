def isInc(n):
    dig = 10
    while n:
        if  n % 10 <= dig:
            dig = n % 10
            n //= 10
        else:
            return False
    return True
    
def isDec(n):
    dig = -1
    while n:
        if  n % 10 >= dig:
            dig = n % 10
            n //= 10
        else:
            return False
    return True

count = 0    
perc = 0

i = 1
while True:
    if not isInc(i) and not isDec(i):
        count += 1
        perc = float(count) / i
    if perc == 0.99:
        print i
        break
    else:
        i += 1
    