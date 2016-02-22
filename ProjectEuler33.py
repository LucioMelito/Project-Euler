def cancFraction(x, y):
    if x == y:
        return False
    
    commonNum = ''
    
    for num in str(x):
        if num in str(y):
            commonNum = num
    
    if commonNum == '' or commonNum == '0':
        return False
    else:
        newX = str(x).replace(commonNum, '')
        newY = str(y).replace(commonNum, '')
        
    if newX == '0' or newY == '0' or newX == '' or newY == '':
        return False
        
    if int(newX)/float(newY) == x/float(y):
        return True
    else:
        return False
        
pairs = []

for i in range(10,100):
    for j in range(i,100):
        if cancFraction(i,j):
            pairs.append([i,j])
            
print pairs