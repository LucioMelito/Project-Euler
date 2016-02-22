from math import log
import string

f = open('/Users/luciomelito/Documents/Python/Project Euler/p099_base_exp.txt').read().splitlines()

pairs = []

for line in f:
    line = string.split(line, ',')
    line = map(int, line)
    pairs.append(line)
    
res = 0
i = 1

for pair in pairs:
    if pair[1]*log(pair[0]) > res:
        res = pair[1]*log(pair[0])
        idx = i
    i += 1
    
print idx