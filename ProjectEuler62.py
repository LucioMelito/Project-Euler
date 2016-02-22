def makeLargest(n):
    lst = [i for i in str(n)]
    lst.sort(reverse=True)
    newN = int(''.join(lst))
    return newN
    
dic = {}
i = 500

while True:
    n = makeLargest(i**3)
    try: 
        dic[n] += 1
    except:
        dic[n] = 1
        
    if dic[n] == 5:
        cube = n
        break
    else:
        i += 1
        
i = 500

while True:
    n = makeLargest(i**3)
    if n == cube:
        print i**3
        break
    else:
        i += 1