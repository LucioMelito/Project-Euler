from Euler import primes

top = 50000000
top1 = int(top**(0.5))

p = primes(top1)

for i in range(len(p)):
    if p[i]**3 < top:
        ind2 = i
    if p[i]**4 < top:
        ind3 = i

nums = []

for i in p:
    for j in p[:ind2+1]:
        for k in p[:ind3+1]:
            num = i**2 + j**3 + k**4
            if num < 50000000:
                nums.append(num)
           
print len(set(nums))