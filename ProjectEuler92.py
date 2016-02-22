# quite slow
import time

start = time.time()

def newNum(n):
    return sum([int(dig)**2 for dig in str(n)])
    
def chain(n, l):
    if n in l:
        return n, l
    else:
        l.append(n)
        return chain(newNum(n), l)
        
eightynine = []

for i in range(1,568):
    if 89 in chain(i,[])[1]:
        eightynine.append(i)

count = len(eightynine)        
                        
for i in range(568, 10000000):
    while i > 567:
        i = newNum(i)
        if i in eightynine:
            count += 1

end = time.time() - start            
                                    
print count, end
