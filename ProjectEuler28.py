tot = 1
dim = 1001

nIt = (dim - 1)*2

diff = 0
current = 1
for i in range(nIt):
    if i % 4 == 0:
        diff += 2
    current += diff
    tot += current
    
print tot