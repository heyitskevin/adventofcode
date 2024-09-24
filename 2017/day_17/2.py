FILENAME = 'input.txt'

def readfile():
    with open(FILENAME) as f:
        return int(f.read().strip())
    

def func():
    steps = readfile()
    
    b = [0]
    v = 1
    ix = 0
    curr = -1
    while v < 50000001:
        ix += steps
        ix = ix % v
        ix += 1
        if ix == 1:
            curr = v
        # b.insert(ix, v)
        v += 1
    return curr

print(func())