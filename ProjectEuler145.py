import time

start = time.time()

def reverse(num):
    if num % 10 == 0:
        return False
    rev = 0
    while(num > 0):
        rev = (10*rev)+num%10
        num //= 10
    return rev
    
def isRev(n):
    N = reverse(n)
    if not N:
        return False
    n = n + N
    while n:
        if n % 2 == 0:
            return False
        n /= 10
    return True    
    
count = 0
for i in xrange(1, 10000000):
    if isRev(i):
        count += 1

time = time.time() - start        
        
print count, time