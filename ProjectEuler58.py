from Euler import isPrime
    
dim = 100000

def solve():

    diff = 2
    current = 9
    count = 3
    for i in range(4, dim):
        if i % 4 == 0:
            diff += 2
            if count / float(i+1) < 0.10:
                return i, current
        current += diff
        if isPrime(current):
            count += 1

result = solve()            
print ((result[0] / 2) + 1), result[1]