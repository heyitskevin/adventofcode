FILENAME = 'input.txt'

def readfile():
    res = {}
    with open(FILENAME) as f:
        for ln in f.read().split('\n'):
            a, b = ln.split(':')
            res[int(a)] = int(b)
    return res
    

def func():
    data = readfile()
    offset = 0
    sev = False
    while not sev:
        sev = True
        for l in data.keys():
            d = data[l]
            if (l + offset) % (2 * d - 2) == 0:
                sev = False
                offset += 1
                break
    return offset

print(func())