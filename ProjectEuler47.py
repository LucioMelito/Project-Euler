from Euler import factor
    
def distinctFact(a, b):
    if len(a) != 4 or len(b) != 4:
        return False
    return True
    
def solve():
    i = 1000
    while True:
        print i
        a,b,c,d = factor(i), factor(i+1), factor(i+2), factor(i+3)
        if distinctFact(a,b) and distinctFact(a,c) and distinctFact(a,d) and distinctFact(b,c) \
        and distinctFact(b,d) and distinctFact(c,d):
            return i
        else:
            i += 1