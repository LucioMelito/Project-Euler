from Euler import primesNP

primes = list(primesNP(10000))

prod = 1
for i in range(0, 7):
    prod *= primes[i]
    
print prod

# we want a big number with a small totient, and this happens when the number is
# the product of the first n-primes. Highest number below one million which satisfies
# this is 510510 (2*3*5*7*11*13*17)