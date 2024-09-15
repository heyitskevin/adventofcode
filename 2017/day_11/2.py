FILENAME = 'input.txt'

def readfile():
    with open(FILENAME) as f:
        return f.read().strip().split(',')
    

def func():
    dist = 0
    inst = readfile()
    
    ns = 0
    d1 = 0
    d2 = 0
    for i in inst:
        if i == 'n':
            ns += 1
        if i == 's':
            ns -= 1
        if i == 'ne':
            d1 += 1
        if i == 'sw':
            d1 -= 1
        if i == 'nw':
            d2 += 1
        if i == 'se':
            d2 -= 1
        nd = abs(ns) + abs(max(d1,d2))
        dist = max(dist, nd)
    return dist


print(func())