def isPal(n):
    if len(n) < 2:
        return True
    else:
        return n[0] == n[-1] and isPal(n[1:-1])
        
def newNum(n):
    return n + int(str(n)[::-1])
    
def chain(n):
    i = 50
    while i > 1:
        if isPal(str(newNum(n))):
            return True
        else:
            n = newNum(n)
            i -= 1
    return False
            
count = 0
for i in range(1, 10000):
    if chain(i):
        count += 1
        
print 9999 - count