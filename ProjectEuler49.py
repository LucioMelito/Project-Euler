from Euler import primes
from itertools import permutations

primes = primes(10000)
primeStr = map(str, primes)

perms = []
for prime in primeStr:
    tempList = list(permutations(prime))
    newList = []
    for item in tempList:
        if int(''.join(item)) in primes:
            newList.append(int(''.join(item)))
    newList = list(set(newList))
    if len(newList) >= 3:
        perms.append(newList)

valid = []    
    
for perm in perms:
    combs = list(permutations(perm, 3))
    for comb in combs:
        comb = list(comb)
        comb.sort()
        if comb[2] - comb[1] == comb[1] - comb[0]:
            valid.append(str(comb[0])+str(comb[1])+str(comb[2]))
            
print list(set(valid))