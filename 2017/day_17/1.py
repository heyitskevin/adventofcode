FILENAME = 'input.txt'

def readfile():
    with open(FILENAME) as f:
        return int(f.read().strip())
    

def func():
    steps = readfile()
    
    b = [0]
    v = 1
    ix = 0
    while v < 2018:
        ix += steps
        ix = ix % len(b)
        ix += 1
        
        b.insert(ix, v)
        v += 1
    return b[ix + 1]

print(func())