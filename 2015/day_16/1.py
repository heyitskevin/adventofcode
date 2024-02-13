FILENAME = 'input.txt'

TICKERNAME = 'tape.txt'

def readticker():
    d = {}
    with open(TICKERNAME) as t:
        for ln in t.read().split('\n'):
            k, v = ln.split(': ')
            d[k] = int(v)
    return d

def readfile():
    r = []
    with open(FILENAME) as f:
        for ln in f.read().split('\n'):
            aunt_number, rest = ln[3:].split(':', 1)
            d = {}
            for att in rest.split(','):
                name, num = att.strip().split(':')
                d[name] = int(num)
            r.append((int(aunt_number), d))
    return r



def func():
    t = readticker()
    aunts = readfile()
    for a, data in aunts:
        match = True
        for k, v in t.items():
            if k in data and data[k] != v:
                match = False
                break
            elif k not in data:
                continue
        if match:
            print('aunt', a)
            

func()