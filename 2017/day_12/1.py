FILENAME = 'input.txt'

def readfile():
    res = {}
    with open(FILENAME) as f:
        for ln in f.read().split('\n'):
            a, b = ln.strip().split(' <-> ')
            res[int(a)] = [int(v.strip()) for v in b.split(',')]

    return res

def func():
    prog = readfile()
    visited = set()
    q = [0]
    while q:
        c = q.pop(0)
        visited.add(c)
        children = prog[c]
        for x in children:
            if x not in visited:
                q.append(x)

    return len(visited)


print(func())