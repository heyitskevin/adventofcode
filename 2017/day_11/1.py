FILENAME = 'input.txt'

from collections import Counter
def readfile():
    with open(FILENAME) as f:
        return f.read().strip().split(',')
    

def func():
    inst = readfile()

    c = Counter(inst)
    ns = c['n'] - c['s']
    d1 = c['ne'] - c['sw']
    d2 = c['nw'] - c['se']
    return ns + max(d1,d2)

print(func())

703 - 737