# ugly and stupid
import math

def divisors(x):
    divList = []
    y = 1
    while y <= math.sqrt(x):
        if x % y == 0:
            divList.append(y)
            divList.append(int(x / y))
        y += 1
    if x in divList:
        divList.remove(x)
    return list(set(divList))
    
def isAbundant(x):
    if sum(divisors(x)) > x:
        return True
    else:
        return False
        
abundantNums = []
for i in range(28124):
    if isAbundant(i):
        abundantNums.append(i)
        
possibleSums = []
for i in range(len(abundantNums)):
    for j in range(i, len(abundantNums)):
        possibleSums.append(abundantNums[i]+abundantNums[j])
possibleSums = list(set(possibleSums))

result = 0
for i in range(1,28124):
    if i not in possibleSums:
        result += i
        
print result   