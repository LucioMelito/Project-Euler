i = 1000000
nums = []
count = 0

for base in range(1, 10):
    for exp in range(1, 1000):
        if len(str(base**exp)) == exp:
            count += 1
            nums.append(base**exp)
            
print count