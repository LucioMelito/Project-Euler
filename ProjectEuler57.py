numerator = 1
denominator = 2

count = 0

for i in range(2, 1000):
    temp = numerator
    numerator = denominator
    denominator = 2*numerator + temp
    if len(str(denominator + numerator)) > len(str(denominator)):
        count += 1
        
print count
    