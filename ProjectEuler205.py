peter = {}
colin = {}

for a in range(1,5):
    for b in range(1,5):
        for c in range(1,5):
            for d in range(1,5):
                for e in range(1,5):
                    for f in range(1,5):
                        for g in range(1,5):
                            for h in range(1,5):
                                for i in range(1,5):
                                    s = a+b+c+d+e+f+g+h+i
                                    try:
                                        peter[s] += 1
                                    except:
                                        peter[s] = 1
                                        
for a in range(1,7):
    for b in range(1,7):
        for c in range(1,7):
            for d in range(1,7):
                for e in range(1,7):
                    for f in range(1,7):
                        s = a+b+c+d+e+f
                        try:
                            colin[s] += 1
                        except:
                            colin[s] = 1
                        
totPeter = float(sum(peter.values()))
totColin = float(sum(colin.values()))

prob = 0

for i in peter:
    for j in colin:
        if i > j:
            prob += peter[i]/totPeter*colin[j]/totColin
        
print prob