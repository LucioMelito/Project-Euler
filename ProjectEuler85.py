import sys
sys.setrecursionlimit(200000)

def rec(i, j):
    if j == 1:
        return i*(i+1)/2
    else:
        return i*(i+1)/2*j + rec(i, j-1)
        

diff = 2000000
pair = []

for i in range(50, 200):
    for j in range(1, 200):
        if abs(rec(i, j) - 2000000) < diff:
            diff = abs(rec(i, j) - 2000000)
            pair = [i, j]
            
print diff, pair, pair[0]*pair[1]