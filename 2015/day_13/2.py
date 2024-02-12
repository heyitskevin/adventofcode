FILENAME = 'input.txt'
from itertools import permutations
from collections import defaultdict
def read_file():
    r = []
    with open(FILENAME) as f:
        for ln in f.read().split('\n'):
            first = ln.split('would')[0].strip()
            last = ln.split('sitting next to')[-1].strip()[:-1]
            units = ln.split('would')[1].split('happiness')[0].strip()
            sign, val = units.split(' ')
            if sign == 'lose':
                val = int(val) * -1
            else:
                val = int(val)
            r.append((first, last, val))
    
    return r

def unique_positions(elems):
    """
    given a list of elements find the list of unique circular arrangements
    - pick an element as a pivot
    - (N-1)! remaining positional combinations
    - postpend pivot to represent cycle
    """
    pos = []
    pivot = elems[0]
    rest = elems[1:]
    for cc in permutations(rest):
        pos.append([pivot] + list(cc) + [pivot])
    return pos

def func():
    data = read_file()
    names = set()
    d = defaultdict(dict)
    for r in data:
        person, neighbor, val = r
        names.add(person)
        d[person][neighbor] = val
    names.add('me')
    
    for p in list(d.keys()):
        d['me'][p] = 0
        d[p]['me'] = 0
    up = unique_positions(list(names))
    scores = []
    for seq in up:
        scr = 0
        for p_ix in range(len(seq) - 1):
            pp = seq[p_ix]
            n1 = seq[p_ix + 1]
            if p_ix == 0:
                n2 = seq[-2]
            else:
                n2 = seq[p_ix - 1]
            scr += d[pp][n1]
            scr += d[pp][n2]
        scores.append(scr)
    print(max(scores))
            

func()