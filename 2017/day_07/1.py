FILENAME = 'input.txt'

def read_file():
    res = {}
    with open(FILENAME) as f:
        for ln in f.read().split('\n'):
            if ' -> ' in ln:
                k, v = ln.split(' -> ')
                parent = k.split(' (')[0]
                children = v.split(', ')
                res[parent] = children
    return res

def func():
    d = read_file()
    p = set(d.keys())
    c = set()
    for v in d.values():
        for vv in v:
            c.add(vv)
    return p - c

print(func())