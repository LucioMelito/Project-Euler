from math import sqrt
import time

x = time.time()

start = int(sqrt(1121314151617181910))
end = int(sqrt(1929394959697989990)) + 1

print end - start
    
for i in xrange(start,end, 10):
    if str(i ** 2)[::2] == "1234567890":
        print i
        break
        
y = time.time() - x
print y