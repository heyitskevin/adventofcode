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
    vg = set()
    groups = 0

    for p, v in prog.items():
        if p not in vg:
            visited = set()
            groups += 1
            q = [p]
            while q:
                curr = q.pop(0)
                children = prog[curr]
                visited.add(curr)
                for c in children:
                    if c not in visited:
                        q.append(c)
            vg |= visited
        else:
            continue

    return groups

print(func())