import time
from math import factorial
from Euler import multCoeff

start = time.time()

def newNum(n):
    """Return the sum of factorials of the base-10 digits of n."""
    total = 0
    while n:
        total += factorial(n % 10)
        n //= 10
    return total
    
def chain(n, l):
    if n in l:
        return len(l)
    else:
        l.append(n)
        return chain(newNum(n), l)
        
count = 0

for i in range(1,1000000):
    if chain(i, []) == 60:
        count += 1

end = time.time() - start        
                        
print count, end

# actual result 402