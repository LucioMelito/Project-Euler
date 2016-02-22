pents = []

for n in range(1, 5000):
    pents.append(n*(3*n-1)/2)
    
pset = set(pents)
    
solutions = []

for i in range(len(pents)-1):
    for j in range(i+1, len(pents)):
        if (pents[j] - pents[i]) in pset and (pents[j] + pents[i]) in pset:
            solutions.append(pents[j] - pents[i])
            
            
print min(solutions)