import time
from itertools import permutations

start = time.time()

def newNum(n):
    """Return the sum of squares of the base-10 digits of n."""
    total = 0
    while n:
        total += (n % 10) ** 2
        n //= 10
    return total
    
def chain(n, l):
    if n in l:
        return n, l
    else:
        l.append(n)
        return chain(newNum(n), l)
        
nums = {}

for i in range(1,10000000):
    new = newNum(i)
    try:
        nums[new] += 1
    except:
        nums[new] = 1
        
count = 0   

for i in nums:
    if 89 in chain(i,[])[1]: 
        count += nums[i]

end = time.time() - start            
                                    
print count, end