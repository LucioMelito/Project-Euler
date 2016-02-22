from math import factorial
import numpy as np 
from math import sqrt; from itertools import count, islice


def isPrime(n):
    if n < 2: return False
    return all(n%i for i in islice(count(2), int(sqrt(n)-1)))

def factor(n):
    """
    find the prime factors of n along with their frequencies. Example:

    >>> factor(786456)
    [(2,3), (3,3), (11,1), (331,1)]
    """
    if n in [-1, 0, 1]: return []
    if n < 0: n = -n
    F = []
    while n != 1:
         p = trial_division(n)
         e = 1
         n /= p
         while n%p == 0:
             e += 1; n /= p
         F.append((p,e))
    F.sort()
    return F
 
 
def trial_division(n, bound=None):
     if n == 1: return 1
     for p in [2, 3, 5]:
         if n%p == 0: return p
     if bound == None: bound = n
     dif = [6, 4, 2, 4, 2, 4, 6, 2]
     m = 7; i = 1
     while m <= bound and m*m <= n:
         if n%m == 0:
             return m
         m += dif[i%8]
         i += 1
     return n
     
    
    
def primes(n):
    # http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Input n>=6, Returns a list of primes, 2 <= p < n """
    correction = (n%6>1)
    n = {0:n,1:n-1,2:n+4,3:n+3,4:n+2,5:n+1}[n%6]
    sieve = [True] * (n/3)
    sieve[0] = False
    for i in xrange(int(n**0.5)/3+1):
      if sieve[i]:
        k=3*i+1|1
        sieve[      ((k*k)/3)      ::2*k]=[False]*((n/6-(k*k)/6-1)/k+1)
        sieve[(k*k+4*k-2*k*(i&1))/3::2*k]=[False]*((n/6-(k*k+4*k-2*k*(i&1))/6-1)/k+1)
    return [2,3] + [3*i+1|1 for i in xrange(1,n/3-correction) if sieve[i]]
    
   
def primesNP(n):
    # http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Input n>=6, Returns a array of primes, 2 <= p < n """
    sieve = np.ones(n/3 + (n%6==2), dtype=np.bool)
    sieve[0] = False
    for i in xrange(int(n**0.5)/3+1):
        if sieve[i]:
            k=3*i+1|1
            sieve[      ((k*k)/3)      ::2*k] = False
            sieve[(k*k+4*k-2*k*(i&1))/3::2*k] = False
    return np.r_[2,3,((3*np.nonzero(sieve)[0]+1)|1)]
    


def arePerm(x, y):
    x , y = str(x), str(y)
    if len(x) != len(y):
        return False
    if len(x) == 1:
        return x == y
    else:
        return x[0] in y and arePerm(x[1:], y.replace(x[0], ''))
        
        
        
def multCoeff(x):
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    f = 0
    g = 0
    h = 0
    i = 0
    for j in str(x):
        if j == '1':
            a += 1
        elif j == '2':
            b += 1
        elif j == '3':
            c += 1
        elif j == '4':
            d += 1
        elif j == '5':
            e += 1
        elif j == '6':
            f += 1
        elif j == '7':
            g += 1
        elif j == '8':
            h += 1
        elif j == '9':
            i += 1
    num = factorial(a+b+c+d+e+f+g+h+i)
    den = factorial(a)*factorial(b)*factorial(c)*factorial(d)*factorial(e)\
    *factorial(f)*factorial(g)*factorial(h)*factorial(i)
    return num/den