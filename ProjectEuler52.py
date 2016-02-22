def arePerm(x, y):
    x , y = str(x), str(y)
    if len(x) != len(y):
        return False
    if len(x) == 1:
        return x == y
    else:
        return x[0] in y and arePerm(x[1:], y.replace(x[0], ''))
        
def fun():
    i = 10
    while True:
        if arePerm(i, 2*i) and arePerm(i, 3*i) and arePerm(i, 4*i) and arePerm(i, 5*i) and arePerm(i, 6*i):
            return i
        else:
            i += 1        