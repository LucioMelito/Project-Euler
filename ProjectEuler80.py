from decimal import *
getcontext().prec = 102

nums = range(2, 100)
nums.remove(4)
nums.remove(9)
nums.remove(16)
nums.remove(25)
nums.remove(36)
nums.remove(49)
nums.remove(64)
nums.remove(81)

total = 0

for num in nums:
    root = str(Decimal(num).sqrt() * 10**99)[:100]
    s = sum([int(i) for i in root])
    print s
    total += s
    
print total