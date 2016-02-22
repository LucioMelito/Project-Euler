from itertools import permutations

pandigitals = list(permutations('0123456789'))

# more efficient to do the checks the other way around
def hasProp(n):
    if int(n[7]+n[8]+n[9]) % 17 == 0 and int(n[6]+n[7]+n[8]) % 13 == 0 and int(n[5]+n[6]+n[7]) % 11 == 0 and int(n[4]+n[5]+n[6]) % 7 == 0 \
    and int(n[3]+n[4]+n[5]) % 5 == 0 and int(n[2]+n[3]+n[4]) % 3 == 0 and int(n[1]+n[2]+n[3]) % 2 == 0: 
        return True
    else: 
        return False

nums = []        
                        
for num in pandigitals:
    if hasProp(num):
        nums.append(num)
        
def convert(numList):          
    s = ''.join(numList)          
    s = int(s)              
    return s

ints = []    
for num in nums:
    ints.append(convert(num))
    
print sum(ints)