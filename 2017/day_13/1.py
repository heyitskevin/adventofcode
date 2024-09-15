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
    s = max(data.keys())
    scan = []
    for k in range(s):
        scan.append(data.get(k, 0))
    
    time = 0
    sev = 0
    for layer, depth in enumerate(scan):
        if depth == 0:
            time += 1
            continue
        
        p_scanner = time % (2*(depth - 1))
        
        if p_scanner == 0:
            sev += (layer * depth)
        time += 1
    return sev

print(func())